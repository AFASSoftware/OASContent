import os
import json
from typesense import Client
from dotenv import load_dotenv
from pathlib import Path
import frontmatter
from datetime import date

# Load environment variables from .env file
load_dotenv()

# Map the environment variables to constants
TYPESENSE_HOST = os.getenv('TYPESENSE_HOST')
TYPESENSE_SEARCH_API_KEY = os.getenv('TYPESENSE_SEARCH_API_KEY')
TYPESENSE_COLLECTION = os.getenv('TYPESENSE_COLLECTION')

if not all([TYPESENSE_HOST, TYPESENSE_SEARCH_API_KEY, TYPESENSE_COLLECTION]):
    raise ValueError("One or more environment variables are not set")

# Initialize Typesense client
client = Client({
    'nodes': [{
        'host': TYPESENSE_HOST,
        'port': '443',
        'protocol': 'https'
    }],
    'api_key': TYPESENSE_SEARCH_API_KEY,
    'connection_timeout_seconds': 300  # Increase the timeout for imports
})

directory_path = Path(__file__).resolve().parents[1] / 'markdownpages'

def date_converter(o):
    if isinstance(o, date):
        return o.isoformat()
    return o


def read_markdown_files(directory):
    jsonl_data = []
    processed_files = 0
    skipped_files = 0

    print(f"Starting to process markdown files in directory: {directory}")
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                print(f"Processing file: {file_path}")

                # Attempt to read the file with different encodings
                file_content = None
                for encoding in ['utf-8', 'latin-1', 'utf-16']:
                    try:
                        with open(file_path, 'r', encoding=encoding) as f:
                            file_content = f.read()
                        break  # Exit the loop if reading is successful
                    except UnicodeDecodeError:
                        continue  # Try the next encoding

                if file_content is None:
                    print(f"Error reading file {file_path}: Unable to decode with tried encodings")
                    skipped_files += 1
                    continue

                # Extract the language and product from the path
                relative_path = file_path.relative_to(directory)
                parts = relative_path.parts
                
                # Handle different directory structures
                if len(parts) >= 3:
                    # Structure: Product/Language/file.md
                    product = parts[0]
                    language = parts[1]
                elif len(parts) == 2:
                    # Structure: Product/file.md (no language subfolder)
                    product = parts[0]
                    language = 'en'  # Default to English
                else:
                    # Structure: file.md (root level)
                    product = 'unknown'
                    language = 'en'
                
                print(f"  Product: {product}, Language: {language}, Parts: {parts}")

                # Updated product filtering to include all valid products
                valid_products = ['profit', 'sb', 'endpoint', 'home', 'main', 'spec']
                if product not in valid_products:
                    print(f"  Skipping file - product '{product}' not in allowed list: {valid_products}")
                    skipped_files += 1
                    continue

                # Only filter by language if we're in a language-specific folder
                if len(parts) >= 3 and language not in ['en', 'nl']:
                    print(f"  Skipping file - language '{language}' not supported")
                    skipped_files += 1
                    continue

                # Parse the markdown content and extract front matter
                try:
                    post = frontmatter.loads(file_content)
                    content = post.content
                    data = post.metadata
                except Exception as e:
                    print(f"  Error parsing frontmatter for {file_path}: {e}")
                    skipped_files += 1
                    continue

                # Check if the file should be indexed
                indexable = data.get('index', True)
                if indexable is False:
                    print(f"  Skipping file - marked as non-indexable")
                    skipped_files += 1
                    continue

                # Extract the paths from the file path
                relative_path = file_path.relative_to(directory)
                extracted_path = str(relative_path).replace('.md', '').replace('\\', '/')
                
                # Clean up the path for consistent formatting
                if extracted_path.startswith('/'):
                    extracted_path = extracted_path[1:]

                # Check if tags has a value
                if 'tags' in data:
                    if isinstance(data['tags'], str):
                        data['tags'] = data['tags'].split(', ')

                # Extract the title and remove trailing spaces, newlines, and carriage returns
                if 'title' in data:
                    title = data['title']
                elif content and content.strip():
                    # Extract title from first line if no title in frontmatter
                    first_line = content.split('\n')[0].replace('# ', '').replace('\r', '').strip()
                    title = first_line if first_line else file_path.stem
                else:
                    title = file_path.stem

                # Create a JSON object with the extracted data and content
                json_object = {
                    'id': f"{file_path.stem}_{language}_{product}".replace(' ', '_'),
                    'topic': data.get('topic', ''),
                    'tags': data.get('tags', []),
                    'title': title,
                    'content': content,
                    'path': extracted_path,
                    'language': language,
                    'category': data.get('category', ''),
                    'product': product,
                    'type': 'markdown',
                    'version': '',
                    'author': data.get('author', ''),
                    'date': data.get('date', '').isoformat() if isinstance(data.get('date', ''), date) else data.get('date', '')
                }
                
                # Add the JSON object directly to the list (not as a JSON string)
                jsonl_data.append(json_object)
                processed_files += 1
                print(f"  Successfully processed file: {file_path.name}")

    print(f"Processing complete. Processed: {processed_files}, Skipped: {skipped_files}")
    print(f"Total documents to import: {len(jsonl_data)}")
    return jsonl_data

def import_data_to_typesense(jsonl_data):
    if not jsonl_data:
        print("No data to import")
        return
        
    print(f"Attempting to import {len(jsonl_data)} documents to Typesense...")
    try:
        result = client.collections[TYPESENSE_COLLECTION].documents.import_(jsonl_data, {'action': 'create'})
        print('Data imported successfully')
        print(result)
    except Exception as e:
        print('Error importing data to Typesense:', e)
        # Print more details about the error
        if hasattr(e, 'response'):
            print('Response:', e.response)
        raise

def write_jsonl_to_file(jsonl_data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for json_line in jsonl_data:
            f.write(json.dumps(json_line) + '\n')

if __name__ == '__main__':
    print(f"Directory path: {directory_path}")
    print(f"Directory exists: {directory_path.exists()}")
    
    jsonl_data = read_markdown_files(directory_path)
    
    # Optionally write to file for debugging
    # write_jsonl_to_file(jsonl_data, 'markdown_debug_output.jsonl')
    
    if jsonl_data:
        import_data_to_typesense(jsonl_data)
    else:
        print("No markdown data to import")
