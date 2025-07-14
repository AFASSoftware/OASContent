import os
import json
import markdown
import markdown.htmlparser
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
    'connection_timeout_seconds': 2
})

directory_path = Path(__file__).resolve().parents[1] / 'MarkdownPages'

def date_converter(o):
    if isinstance(o, date):
        return o.isoformat()
    return o


def read_markdown_files(directory):
    jsonl_data = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file

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
                    continue

                # Extract the language and product from the path
                relative_path = file_path.relative_to(directory)
                parts = relative_path.parts
                language = parts[1] if len(parts) > 1 else ''
                product = parts[0] if len(parts) > 0 else ''

                if product == 'Profit' or product == 'sb':
                    # continue with code
                    pass
                else:
                    continue

                if language != 'en' and language != 'nl':
                    continue

                # Parse the markdown content and extract front matter
                post = frontmatter.loads(file_content)
                content = post.content
                data = post.metadata

                # Check if the file should be indexed
                indexable = data.get('index', True)
                if indexable is False:
                    continue

                # Extract the paths from the file path
                docs_index = str(file_path).find("\\MarkdownPages")
                extracted_path = str(file_path)[docs_index + 15:].replace('.md', '').replace('/runner/work/API-Documentation/API-Documentation/MarkdownPages/','')
                extracted_path = extracted_path.replace('ork/OAS3Content/OAS3Content/MarkdownPages/', '/')

                # Check if tags has a value
                if 'tags' in data:
                    if isinstance(data['tags'], str):
                        data['tags'] = data['tags'].split(', ')

                # Extract the title and remove trailing spaces, newlines, and carriage returns
                title = data.get('title', content.split('\n')[0].replace('# ', '').replace('\r', '').strip())

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
                
                # Convert the JSON object to a JSON string, ensuring proper escaping
                jsonl_data.append(json.dumps(json_object, default=date_converter))

    return '\n'.join(jsonl_data)

def import_data_to_typesense(jsonl_data):
    try:
        result = client.collections[TYPESENSE_COLLECTION].documents.import_(jsonl_data, {'action': 'create'})
        print('Data imported successfully')
        print(result)
    except Exception as e:
        print('Error importing data to Typesense:', e)

if __name__ == '__main__':
    jsonl_data = read_markdown_files(directory_path)
    import_data_to_typesense(jsonl_data)
