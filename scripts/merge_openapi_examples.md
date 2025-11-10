# OpenAPI Examples and Responses Merge Script

This script merges OpenAPI examples and response definitions from markdown documentation into OpenAPI specification files.

## Overview

The `merge_openapi_examples.py` script automatically extracts code examples and response definitions from markdown files and merges them into the corresponding OpenAPI specification files. This ensures that examples and responses in the documentation are synchronized with the API specifications.

## Prerequisites

Install and prepare python usage

Before running the merge script, ensure you have the latest OpenAPI specifications:

1. **Download Latest API Specs**: Get the most recent API specifications from:
   ```
   https://stable.testafasfocus.ad.afas.nl:401/admin/api/release-spec
   ```
   and place the file in OASContent\OpenApiSpecs\sb\nl\release-spec.json
2. **Update Local Specs**: Place the downloaded specifications in your OpenAPI directory
3. **Verify Specs**: Ensure the spec files are valid and up-to-date before merging examples

## OpenAPI Specification Structure

The OpenAPI specifications are organized in the following structure (see `D:\Anta\OASContent\OpenApiSpecs\sb\files`):

```
OpenApiSpecs/
└── sb/
    └── files/
        ├───getconnector-vattypes-get-1.0/
        │   └───responses/
        │           vattypes.json
        │
        ├───updateconnector-address-Post-1.0/
        │   ├───examples/
        │   │       New addres for organisation.json
        │   │       New addres for person.json
        │   │       New address DE.json
        │   │
        │   └───responses/
        │           success.json
        │
        └───[endpoint-name-method-version]/
            ├───examples/           # Request/response examples (optional)
            └───responses/          # Response definitions (optional)
```

Each endpoint is organized in its own directory following the naming pattern:
- `{connector}-{endpoint}-{method}-{version}`
- Examples: `getconnector-vattypes-get-1.0`, `updateconnector-address-Post-1.0`

Within each endpoint directory:
- **examples/**: Contains JSON files with request and response examples
- **responses/**: Contains JSON files with response definitions

**Note**: The English (EN) and Dutch (NL) OpenAPI specifications are identical. The API specifications are language-agnostic as they define the technical structure of the API. Language-specific content (descriptions, documentation) is handled separately in the markdown documentation files.

The script can merge content into:
- **Examples**: Request/response example JSON files in the `examples/` subdirectory
- **Responses**: Response definition JSON files in the `responses/` subdirectory

## Usage

### Basic Usage
```bash
python D:\Anta\OASContent\scripts\merge_openapi_examples.py `
  D:\Anta\OASContent\OpenApiSpecs\sb\nl\release-spec.json `
  D:\Anta\OASContent\OpenApiSpecs\sb\files `
  --out D:\Anta\OASContent\OpenApiSpecs\sb\nl\release-spec.merged.json
```

### Advanced Usage
```bash
# Specify custom paths
python merge_openapi_examples.py --markdown-dir ./docs --openapi-dir ./specs

# Dry run (preview changes without modifying files)
python merge_openapi_examples.py --dry-run

# Verbose output
python merge_openapi_examples.py --verbose

# Show help
python merge_openapi_examples.py --help
```

## How It Works

1. **Get Latest Specs**: Download the current API specifications from the release endpoint
2. **Scans Markdown Files**: Searches for markdown files containing OpenAPI examples and responses
3. **Extracts Content**: Parses code blocks tagged with OpenAPI schema/response references
4. **Validates Content**: Ensures examples and responses match the expected schema format
5. **Merges into Specs**: Updates the corresponding OpenAPI specification files
6. **Reports Results**: Provides a summary of merged content and any errors

## Markdown Format

In your markdown files, use the following format to tag OpenAPI content:

### Examples

````markdown
```json
// openapi: updateconnector-address-Post-1.0/examples/New address DE.json
{
  "KnPerson": {
    "MatchPer": 0,
    "AutoNum": false,
    "Fields": {
      "BcCo": "DE"
    }
  }
}
```
````

### Responses

````markdown
```json
// openapi: updateconnector-address-Post-1.0/responses/success.json
{
  "result": "Succeeded",
  "traceId": "3614178a-f801-47b7-bae1-dad6439f2c54",
  "data": {
      "KnPerson": "fcb31b25-8da1-4a90-ae33-a93d932184f0"
  },
  "errors": []
}
```
````

### Full Path Reference

You can also use the full path from the `files/` directory:

````markdown
```json
// openapi: getconnector-vattypes-get-1.0/responses/vattypes.json
{
  "result": "Succeeded",
  "data": [
    {
      "VatTypeId": "1",
      "Description": "High rate"
    }
  ]
}
```
````

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--markdown-dir` | Directory containing markdown files | `./MarkdownPages` |
| `--openapi-dir` | Directory containing OpenAPI spec files | `./OpenAPI` |
| `--dry-run` | Preview changes without modifying files | `false` |
| `--verbose` | Show detailed output | `false` |
| `--help` | Display help message | - |

## Exit Codes

- `0` - Success (all examples merged successfully)
- `1` - Failure (errors occurred during merge)

## Best Practices

1. **Keep Content Valid**: Ensure all examples and responses are valid JSON
2. **Reference Correct Paths**: Use accurate file paths relative to the `files/` directory
3. **Follow Naming**: Match the exact endpoint directory name (case-sensitive)
4. **Use Descriptive Names**: Example files should have meaningful names describing their use case
5. **Test After Merge**: Validate OpenAPI specs after running the script
6. **Version Control**: Commit both markdown and OpenAPI changes together

## Troubleshooting

### Common Issues

1. **Content Not Merging**
   - Verify the file path is correct and matches the endpoint directory structure
   - Check that the target directory exists (e.g., `updateconnector-address-Post-1.0/examples/`)
   - Ensure JSON syntax is valid (use a JSON validator)

2. **Path Not Found**
   - Confirm the endpoint directory exists in `OpenApiSpecs/sb/files/`
   - Verify the subdirectory (`examples/` or `responses/`) exists
   - Check the exact filename including spaces and capitalization

3. **Invalid Format**
   - Validate JSON syntax (trailing commas, quotes, brackets)
   - Ensure the file extension is `.json`
   - Verify the content matches the expected structure for examples or responses

### Getting Help

- Review the verbose output with `--verbose` flag
- Use `--dry-run` to preview changes before applying
- Check the OpenAPI specification structure
- Contact the development team for assistance
