# IndexTools

## Overview
The IndexTools collection provides Python utilities for managing and populating a Typesense search index with API documentation content. These tools handle the complete lifecycle of search index management for both Markdown documentation and OpenAPI specifications.

## Features
- Create and manage Typesense search collections
- Import Markdown documentation with frontmatter metadata
- Import OpenAPI specification data from JSON files
- Multi-language support (English/Dutch)
- Automatic content extraction and indexing
- Environment-based configuration

## How It Works
The tools work together to create a searchable index of API documentation:

1. **Collection Management**: Create or drop Typesense search collections with predefined schemas
2. **Content Import**: Parse and index Markdown files and OpenAPI specifications
3. **Multi-language Processing**: Handle both English (`en`) and Dutch (`nl`) content
4. **Metadata Extraction**: Extract frontmatter from Markdown files and structure from OpenAPI specs
5. **Search Indexing**: Upload processed content to Typesense for full-text search capabilities

## Files Description
- **CreateCollection.py**: Creates a new Typesense collection with the required schema for documentation search
- **DropCollection.py**: Deletes an existing Typesense collection (useful for resetting the index)
- **ImportApiSpecData.py**: Processes OpenAPI specification files and imports endpoint data to the search index
- **ImportMarkdownData.py**: Parses Markdown documentation files with frontmatter and imports content to the search index
- **requirements.txt**: Python dependencies required for all tools

## Deployment

### Prerequisites
- Python 3.7+
- Typesense server instance
- Access credentials for Typesense
- Environment variables configuration

### Installation/Setup

1. **Install Python dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

2. **Create environment configuration**:
   Create a `.env` file in the project root with:
   ```
   TYPESENSE_HOST=your-typesense-host
   TYPESENSE_SEARCH_API_KEY=your-api-key
   TYPESENSE_COLLECTION=your-collection-name
   ```

3. **Verify file structure**:
   Ensure the following directories exist relative to the scripts folder:
   - `../MarkdownPages/` - Contains documentation Markdown files
   - `../OpenApiSpecs/` - Contains OpenAPI specification files

### Configuration
- **Environment Variables**: Configure Typesense connection details in `.env` file
- **Collection Schema**: Modify schema in `CreateCollection.py` if different field requirements are needed
- **Language Support**: Currently supports English (`en`) and Dutch (`nl`) languages
- **File Encodings**: Tools handle UTF-8, Latin-1, and UTF-16 encodings automatically

## Usage

### Basic Workflow
1. **Create the collection**:
   ```powershell
   python CreateCollection.py
   ```

2. **Import Markdown documentation**:
   ```powershell
   python ImportMarkdownData.py
   ```

3. **Import API specifications**:
   ```powershell
   python ImportApiSpecData.py
   ```

4. **Reset index (if needed)**:
   ```powershell
   python DropCollection.py
   python CreateCollection.py
   ```

### Advanced Usage
- Run imports individually to update specific content types
- Use `DropCollection.py` followed by `CreateCollection.py` for complete index rebuilds
- Monitor console output for import status and error reporting

## Monitoring/Troubleshooting

### Common Issues
- **Environment Variables**: Ensure all required variables are set in `.env` file
- **File Encoding**: Tools automatically try multiple encodings, but check file formats if import fails
- **Typesense Connection**: Verify host, port (443), and API key configuration
- **File Paths**: Ensure relative paths to MarkdownPages and OpenApiSpecs directories are correct

### Error Handling
- Connection timeout increased to 300 seconds for large imports
- Multiple encoding attempts for file reading
- Graceful error handling with descriptive console output
- Validation of required environment variables before execution

## Related Documentation
- [Typesense Documentation](https://typesense.org/docs/)
- [Python-dotenv Configuration](https://pypi.org/project/python-dotenv/)
- [Markdown Frontmatter](https://pypi.org/project/python-frontmatter/)
- OpenAPI Specification processing for API endpoint indexing
