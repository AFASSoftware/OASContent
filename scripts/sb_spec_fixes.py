#!/usr/bin/env python3
"""
Apply manual corrections to a freshly downloaded SB release-spec.json.

The SB spec is generated from the focus repo. Some parts are wrong or incomplete
there and were fixed by hand in earlier releases (8.0). Those hand edits are lost
every time a new release-spec is downloaded, so they live here and can be re-applied.

Each fix reports whether it was applied. A fix that no longer applies (because the
generated spec changed) is reported as SKIPPED: check it and remove it from this
script once the dev team has fixed it at the source.

Usage
------
python scripts/sb_spec_fixes.py OpenApiSpecs/sb/nl/release-spec.json [--out other.json]
"""

import argparse
import json

LEDGERACCOUNTS_PROPERTIES = {
    "Id": {"type": "string", "format": "uuid"},
    "Description": {"type": "string"},
    "LedgerAccountNumber": {"type": "string"},
    "TypeId": {
        "type": "string",
        "format": "uuid",
        "description": "Guid of the ledger account type. See the Type field for the readable label.",
    },
    "InstanceId": {"type": "string", "format": "uuid"},
    "InvestInAsset": {"type": "boolean"},
    "VatAllowed": {"type": "boolean"},
    "MethodKeepingQuantitiesId": {
        "type": "string",
        "format": "uuid",
        "nullable": True,
        "description": "Guid of the quantity-keeping method, or null. See the MethodKeepingQuantities field for the readable label.",
    },
    "Unit1Id": {
        "type": "string",
        "format": "uuid",
        "nullable": True,
        "description": "Guid of the first quantity unit, or null. See the Unit1 field for the readable label.",
    },
    "Unit2Id": {
        "type": "string",
        "format": "uuid",
        "nullable": True,
        "description": "Guid of the second quantity unit, or null. See the Unit2 field for the readable label.",
    },
    "AdministrationId": {"type": "string", "format": "uuid"},
    "Type": {
        "type": "string",
        "description": "Readable label of TypeId.",
        "enum": ["Activa", "Kosten", "Opbrengsten", "Passiva"],
    },
    "MethodKeepingQuantities": {
        "type": "string",
        "description": "Readable label of MethodKeepingQuantitiesId. Empty when no quantities are kept.",
        "enum": ["one", "two", "none", ""],
    },
    "Unit1": {
        "type": "string",
        "description": "Readable label of Unit1Id. Empty when not set.",
        "enum": ["stuks", "kg", "hectare", ""],
    },
    "Unit2": {
        "type": "string",
        "description": "Readable label of Unit2Id. Empty when not set.",
        "enum": ["stuks", "kg", "hectare", ""],
    },
}

BLOB_GET_DESCRIPTION = (
    "Download a blob by its UUID. There are two ways to get access:\n\n"
    "- **With a ReadKey**: pass the `ReadKey` of the blob as query parameter (`?ReadKey=...`) or as `ReadKey` header. "
    "The ReadKey is returned in the `Blob` object of GET endpoints that return attachments. "
    "It works for any user as long as the key is valid, unless the key is bound to an account.\n"
    "- **Without a ReadKey**: only the user that uploaded the blob can download it, and only for about 2 days after the upload. "
    "After that the request fails with \"the preview window has expired\".\n\n"
    "A ReadKey is valid for at least about 3 hours and at most about 28 hours. Do not store it: get a fresh ReadKey from the GET endpoint and download directly. "
    "An expired ReadKey returns \"Expired read token\", a ReadKey for another blob, scope or account returns \"Invalid read token\". "
    "Prefer the `ReadKey` header: a truncated URL (for example by antivirus or VPN software) returns \"the read token was malformed\".\n\n"
    "The blob can only be downloaded after the upload has been completed."
)

BLOB_GET_PARAMETERS = [
    {
        "in": "query",
        "name": "ReadKey",
        "schema": {"type": "string"},
        "required": False,
        "description": "ReadKey of the blob, from the `Blob` object of a GET endpoint. Alternative to the `ReadKey` header.",
    },
    {
        "in": "header",
        "name": "ReadKey",
        "schema": {"type": "string"},
        "required": False,
        "description": "ReadKey of the blob, from the `Blob` object of a GET endpoint. Alternative to the `ReadKey` query parameter.",
    },
]

BLOB_PUT_DESCRIPTION = (
    "Upload a file. The blob UUID must be generated client side. An upload consists of these steps:\n\n"
    "1. **Prepare**: call this endpoint with the `Blob-*` headers and without body. "
    "The response contains the maximum chunk size: `{ \"BlobAccepted\": true, \"ChunkSize\": 5242880 }`.\n"
    "2. **Upload**: call this endpoint without the `Blob-*` headers, with the file content as body.\n"
    "   - File not larger than `ChunkSize`: send the whole file in one request without `Content-Range`. The upload is completed automatically, step 3 is not needed.\n"
    "   - File larger than `ChunkSize`: send the file in chunks, one request per chunk with a `Content-Range` header: `bytes {start}-{end}/{total}` (end is inclusive). "
    "Example for a file of 12582912 bytes: `bytes 0-5242879/12582912`, `bytes 5242880-10485759/12582912`, `bytes 10485760-12582911/12582912`. "
    "When `Content-Length` is sent, it must equal `end - start + 1`. Chunks may be sent in any order and in parallel.\n"
    "3. **Complete** (chunked upload only): call this endpoint without body and with the `x-blob-completed` header (empty value). "
    "Without this step the blob stays incomplete and cannot be used: \"Invalid blob state, the blob upload has not completed\".\n\n"
    "The default maximum size of a blob is 100 MB."
)

BLOB_PUT_PARAMETERS = [
    {
        "in": "header",
        "name": "Content-Range",
        "schema": {"type": "string", "example": "bytes 0-5242879/12582912"},
        "required": False,
        "description": "Only for chunked uploads (step 2): the byte range of this chunk, `bytes {start}-{end}/{total}`. The end is inclusive.",
    },
    {
        "in": "header",
        "name": "x-blob-completed",
        "schema": {"type": "string", "example": ""},
        "required": False,
        "description": "Only for chunked uploads (step 3): send this header with an empty value and without body to complete the upload.",
    },
]

# Enums for the PUT /api/blob/{uuid} headers, first added by hand in 7.4 (commit 75428d0)
BLOB_PUT_HEADER_ENUMS = {
    "Blob-Upload-Type": {
        "schema": {"type": "string", "enum": ["Blob", "Image"], "example": "Blob"},
        "examples": {
            "Blob": {"summary": "For non-image files (e.g. PDF, Word)", "value": "Blob"},
            "Image": {"summary": "For image files (e.g. JPEG, PNG)", "value": "Image"},
        },
    },
    "Blob-Format": {
        "schema": {"type": "string", "enum": ["Default", "Thumb", "Small", "Medium"], "example": "Default"},
        "examples": {
            "Default": {"summary": "Original file (default)", "value": "Default"},
            "Thumb": {"summary": "Thumbnail image", "value": "Thumb"},
            "Small": {"summary": "Small image", "value": "Small"},
            "Medium": {"summary": "Medium image", "value": "Medium"},
        },
    },
}

BLOB_PUT_PREPARE_RESPONSE = {
    "description": "OK. The prepare request (step 1) returns the maximum chunk size in bytes.",
    "content": {
        "application/json": {
            "schema": {
                "type": "object",
                "properties": {
                    "BlobAccepted": {"type": "boolean"},
                    "ChunkSize": {"type": "integer", "description": "Maximum size of one chunk in bytes."},
                },
            },
            "example": {"BlobAccepted": True, "ChunkSize": 5242880},
        }
    },
}

READKEY_DESCRIPTION = (
    "Key to download this blob with GET /api/blob/{uuid}. Valid for a limited time (at least about 3 hours): "
    "do not store it, get a fresh one when you want to download the blob."
)

# Typos in generated descriptions: (wrong, correct)
TEXT_FIXES = [
    ("Vat tarive.", "VAT tariff."),
    ("Make a invoice", "Make an invoice"),
]


def fix_ledgeraccounts(spec):
    """GET /api/ledgeraccounts returns guids plus readable labels, not enum values."""
    try:
        items = spec["paths"]["/api/ledgeraccounts"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]["items"]
    except KeyError:
        return False
    if items.get("properties") == LEDGERACCOUNTS_PROPERTIES:
        return False
    items["properties"] = LEDGERACCOUNTS_PROPERTIES
    return True


def add_parameters(operation, parameters):
    """Add parameters that are not present yet (a parameter is unique by name and location)."""
    existing = {(p.get("name"), p.get("in")) for p in operation.setdefault("parameters", [])}
    added = False
    for parameter in parameters:
        if (parameter["name"], parameter["in"]) not in existing:
            operation["parameters"].append(parameter)
            added = True
    return added


def fix_blob(spec):
    """Document ReadKey (GET) and chunked upload (PUT) on /api/blob/{uuid}."""
    blob = spec.get("paths", {}).get("/api/blob/{uuid}")
    if not blob or "get" not in blob or "put" not in blob:
        return False
    before = json.dumps(blob, sort_keys=True)

    get, put = blob["get"], blob["put"]
    get["description"] = BLOB_GET_DESCRIPTION
    add_parameters(get, BLOB_GET_PARAMETERS)

    put["description"] = BLOB_PUT_DESCRIPTION
    add_parameters(put, BLOB_PUT_PARAMETERS)
    for parameter in put["parameters"]:
        if parameter.get("in") == "header" and parameter.get("name") in BLOB_PUT_HEADER_ENUMS:
            parameter.update(BLOB_PUT_HEADER_ENUMS[parameter["name"]])
    # The prepare and complete requests have no body
    put.setdefault("requestBody", {})["required"] = False
    put["requestBody"]["description"] = "Binary content of the file or chunk (step 2). No body for the prepare (step 1) and complete (step 3) requests."
    put["requestBody"].setdefault("content", {"application/octet-stream": {"schema": {"type": "string", "format": "binary"}}})
    put.setdefault("responses", {})["200"] = BLOB_PUT_PREPARE_RESPONSE

    return json.dumps(blob, sort_keys=True) != before


def fix_readkey_descriptions(node):
    """Explain the ReadKey field in every Blob object, returns the number of changed fields."""
    count = 0
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "ReadKey" and isinstance(value, dict) and "type" in value:
                if value.get("description") != READKEY_DESCRIPTION:
                    value["description"] = READKEY_DESCRIPTION
                    count += 1
            else:
                count += fix_readkey_descriptions(value)
    elif isinstance(node, list):
        for value in node:
            count += fix_readkey_descriptions(value)
    return count


def fix_texts(node):
    """Replace typos in every description, returns the number of replacements."""
    count = 0
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "description" and isinstance(value, str):
                for wrong, correct in TEXT_FIXES:
                    if wrong in value:
                        value = value.replace(wrong, correct)
                        count += 1
                node[key] = value
            else:
                count += fix_texts(value)
    elif isinstance(node, list):
        for value in node:
            count += fix_texts(value)
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("spec", help="Path to release-spec.json")
    parser.add_argument("--out", help="Output path (default: overwrite the input)")
    args = parser.parse_args()

    with open(args.spec, encoding="utf-8") as f:
        spec = json.load(f)

    print("ledgeraccounts response schema:", "APPLIED" if fix_ledgeraccounts(spec) else "SKIPPED (already correct or path missing)")
    print("blob ReadKey and chunked upload:", "APPLIED" if fix_blob(spec) else "SKIPPED (already applied or path missing)")
    count = fix_readkey_descriptions(spec)
    print(f"ReadKey field descriptions: {'APPLIED' if count else 'SKIPPED'} ({count} fields)")
    count = fix_texts(spec)
    print(f"description typos: {'APPLIED' if count else 'SKIPPED'} ({count} replacements)")

    with open(args.out or args.spec, "w", encoding="utf-8", newline="\n") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    main()
