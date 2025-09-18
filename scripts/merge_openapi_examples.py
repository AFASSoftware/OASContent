
#!/usr/bin/env python3
"""
Merge request and response examples into an OpenAPI 3.x spec based on per-operation folders.

Folder layout per operation (folder name equals operationId), for example:
root_dir/
  getconnector-accountingperiod.get-2.0/
    examples/
      example1.json
      example2.json
    responses/
      response1.json
      another.json
      201/
        created.json
      400/
        badrequest.json

Behavior
- Request examples:
  If the operation has a requestBody, files in {op}/examples are merged into
  requestBody.content.<ctype>.examples, keyed by filename (without extension).
  By default only "application/json" is targeted, unless you pass --content-types.
- Response examples:
  Files in {op}/responses are merged into responses. If the folder contains
  status-code subfolders (e.g., 200, 201, 400), those files map to that status code.
  Files directly in {op}/responses map to 200 by default (can be overridden with --default-status).
  Examples go into responses[status].content.<ctype>.examples.
- Existing examples are preserved unless a key conflict occurs, where the file example wins.
- If the spec incorrectly uses a string "example": "<json-string>", it will be upgraded
  into proper structured "examples": { "fromSpec": { "value": <parsed or raw string> } } and
  then merged.

Supported spec formats: YAML or JSON. Requires PyYAML if the input is YAML.

Usage
------
python merge_openapi_examples.py path/to/spec.(yaml|yml|json) path/to/root_dir \
  [--out merged.spec.yaml] [--inplace] [--content-types application/json text/xml] \
  [--default-status 200]

Examples
--------
python merge_openapi_examples.py api.yaml ./ops --inplace
python merge_openapi_examples.py api.json ./ops --out merged.json --content-types application/json
"""

import argparse
import json
import sys
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml  # type: ignore
    _HAVE_YAML = True
except Exception:
    _HAVE_YAML = False

def load_spec(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in (".yaml", ".yml"):
        if not _HAVE_YAML:
            print("ERROR: PyYAML is required to read YAML files. Install with: pip install pyyaml", file=sys.stderr)
            sys.exit(2)
        return yaml.safe_load(text)
    # default to JSON
    return json.loads(text)

def dump_spec(spec: Any, path: Path) -> None:
    if path.suffix.lower() in (".yaml", ".yml"):
        if not _HAVE_YAML:
            print("ERROR: PyYAML is required to write YAML files. Install with: pip install pyyaml", file=sys.stderr)
            sys.exit(2)
        path.write_text(yaml.safe_dump(spec, sort_keys=False, allow_unicode=True), encoding="utf-8")
    else:
        path.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")

def ensure_dict(d: Optional[Dict]) -> Dict:
    return d if isinstance(d, dict) else {}

def ensure_path(container: Dict, *keys: str) -> Dict:
    cur = container
    for k in keys:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    return cur

def parse_json_or_text(p: Path) -> Any:
    text = p.read_text(encoding="utf-8").strip()
    try:
        return json.loads(text)
    except Exception:
        # Not valid JSON; return raw text
        return text

def coerce_string_example_to_examples(content_map: Dict, content_type: str) -> None:
    """
    If content.<ctype>.examples is missing but content.<ctype>.example is present,
    convert it to a named example 'fromSpec'.
    Attempt to parse JSON strings.
    """
    ct = ensure_dict(content_map.get(content_type))
    ex = ct.get("examples")
    single = ct.get("example")
    if ex is None and single is not None:
        value = single
        if isinstance(value, str):
            # Try to parse embedded JSON
            stripped = value.strip()
            # allow cases where JSON is embedded with escaped newlines etc.
            try:
                parsed = json.loads(stripped)
                value = parsed
            except Exception:
                pass
        ct["examples"] = {"fromSpec": {"value": value}}
        # remove the single example
        ct.pop("example", None)
    content_map[content_type] = ct

def merge_examples_into_content(content_map: Dict, content_types: List[str], examples: Dict[str, Any]) -> None:
    for ctype in content_types:
        coerce_string_example_to_examples(content_map, ctype)
        ct = ensure_dict(content_map.get(ctype))
        ct_examples = ensure_dict(ct.get("examples"))
        # file examples override same keys
        for name, val in examples.items():
            ct_examples[name] = {"value": val}
        ct["examples"] = ct_examples
        content_map[ctype] = ct

def collect_files(dirpath: Path) -> List[Path]:
    if not dirpath.exists():
        return []
    files: List[Path] = []
    for p in dirpath.rglob("*"):
        if p.is_file():
            files.append(p)
    return files

def group_response_files(base: Path) -> Dict[str, List[Path]]:
    """
    Returns a mapping of statusCode -> list of files.
    Subdirectories named like digits (e.g., 200, 201, 4XX is also supported as literal) map to that status.
    Files directly under base are returned under key "" for the caller to map to default.
    """
    result: Dict[str, List[Path]] = {}
    if not base.exists():
        return result
    for child in base.iterdir():
        if child.is_dir():
            status = child.name
            result.setdefault(status, [])
            for f in child.rglob("*"):
                if f.is_file():
                    result[status].append(f)
        elif child.is_file():
            result.setdefault("", []).append(child)
    return result

def find_operations(spec: Dict) -> List[Dict]:
    """
    Iterate over all operations under paths and methods.
    Returns list of tuples with (pathKey, methodKey, operationObject).
    """
    ops = []
    paths = ensure_dict(spec.get("paths"))
    for path_key, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        for method_key, opobj in methods.items():
            if not isinstance(opobj, dict):
                continue
            # method must be one of HTTP methods per OpenAPI
            if method_key.lower() not in ("get", "post", "put", "patch", "delete", "options", "head", "trace"):
                continue
            ops.append({"path": path_key, "method": method_key, "op": opobj})
    return ops

def unique_backup_path(path: Path) -> Path:
    base = path.with_suffix(path.suffix + ".bak")
    if not base.exists():
        return base
    i = 1
    while True:
        cand = path.with_suffix(path.suffix + f".bak{i}")
        if not cand.exists():
            return cand
        i += 1

def main():
    parser = argparse.ArgumentParser(description="Merge request/response examples into an OpenAPI spec.")
    parser.add_argument("spec_path", type=Path, help="Path to OpenAPI spec (YAML or JSON).")
    parser.add_argument("root_dir", type=Path, help="Root directory containing per-operation folders (named by operationId).")
    parser.add_argument("--out", type=Path, help="Output file path. If omitted and --inplace not set, writes alongside with .merged suffix.")
    parser.add_argument("--inplace", action="store_true", help="Overwrite the input spec file (a backup .bak is created).")
    parser.add_argument("--content-types", nargs="+", default=["application/json"], help="Content types to target for examples.")
    parser.add_argument("--default-status", default="200", help="Default status code for response files placed directly in 'responses' (no subfolder).")
    args = parser.parse_args()

    spec = load_spec(args.spec_path)
    if not isinstance(spec, dict):
        print("ERROR: Spec root must be an object.", file=sys.stderr)
        sys.exit(2)

    ops = find_operations(spec)
    print(f"Found {len(ops)} operations in the spec.")
    ops_by_operation_id = {}
    for entry in ops:
        opobj = entry["op"]
        op_id = opobj.get("operationId")
        if not isinstance(op_id, str) or not op_id.strip():
          continue
        ops_by_operation_id[op_id] = entry

    # For each operation in the spec, check whether a folder with its operationId exists
    for op_id, entry in ops_by_operation_id.items():
        op_dir = args.root_dir / op_id
        if not op_dir.exists() or not op_dir.is_dir():
            continue  # nothing to merge for this operation

        # 1) Request examples
        examples_dir = op_dir / "examples"
        if examples_dir.exists():
            example_files = [p for p in examples_dir.rglob("*") if p.is_file()]
            print(f"Found {len(example_files)} example files for operationId '{op_id}'")

            example_map: Dict[str, Any] = {}
            for f in example_files:
                key = f.stem
                example_map[key] = parse_json_or_text(f)

            # Ensure requestBody exists when we are about to write examples
            opobj = entry["op"]
            req = ensure_dict(opobj.get("requestBody"))
            content_map = ensure_dict(req.get("content"))
            merge_examples_into_content(content_map, args.content_types, example_map)
            req["content"] = content_map
            opobj["requestBody"] = req
            entry["op"] = opobj

        # 2) Response examples
        responses_dir = op_dir / "responses"
        if responses_dir.exists():
            grouped = group_response_files(responses_dir)
            opobj = entry["op"]
            responses = ensure_dict(opobj.get("responses"))
            print(f"Found {len(responses)} response files for operationId '{op_id}'")

            for status_key, files in grouped.items():
                status = status_key if status_key else args.default_status
                resp_obj = ensure_dict(responses.get(status))

                # Some specs use $ref for responses. If so, materialize a local response object.
                if "$ref" in resp_obj and len(resp_obj) == 1:
                    # Lift the $ref under a local object and add content next to it.
                    # This keeps the ref while allowing us to attach examples to "content".
                    # If your tooling dislikes that, consider resolving refs beforehand.
                    resp_obj = {"$ref": resp_obj["$ref"], "content": {}}

                content_map = ensure_dict(resp_obj.get("content"))
                ex_map: Dict[str, Any] = {}
                for f in files:
                    key = f.stem
                    ex_map[key] = parse_json_or_text(f)
                merge_examples_into_content(content_map, args.content_types, ex_map)
                resp_obj["content"] = content_map
                responses[status] = resp_obj

            opobj["responses"] = responses
            entry["op"] = opobj

    # Write output
    if args.inplace:
        backup = unique_backup_path(args.spec_path)
        backup.write_text(args.spec_path.read_text(encoding="utf-8"), encoding="utf-8")
        dump_spec(spec, args.spec_path)
        print(f"Updated spec written in place. Backup: {backup}")
    else:
        out = args.out
        if out is None:
            # default next to input
            if args.spec_path.suffix.lower() in (".yaml", ".yml"):
                out = args.spec_path.with_suffix(".merged.yaml")
            else:
                out = args.spec_path.with_name(args.spec_path.stem + ".merged.json")
        dump_spec(spec, out)
        print(f"Wrote merged spec to: {out}")

if __name__ == "__main__":
    main()
