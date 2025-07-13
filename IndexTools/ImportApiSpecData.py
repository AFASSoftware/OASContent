import os
import json
import zipfile
from typesense import Client
from dotenv import load_dotenv
from pathlib import Path

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

# Path to the OpenApiSpecs zip file
zip_file_path = Path(__file__).resolve().parents[1] / 'OpenApiSpecs' / 'OpenApiSpecs.zip'
extracted_path = Path(__file__).resolve().parents[1] / 'OpenApiSpecs'

def extract_zip(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def get_highest_version_file(directory):
    highest_version = (0, 0, 0)
    highest_version_file = None

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                try:
                    version_str = file.replace('.json', '')
                    major, minor, patch = map(int, version_str.split('-'))
                    version_tuple = (major, minor, patch)
                    
                    if version_tuple > highest_version:
                        highest_version = version_tuple
                        highest_version_file = Path(root) / file
                except ValueError:
                    continue

    return highest_version_file

def read_openapi_files(directory):
    jsonl_data = []

    # List of languages to check
    languages = ['nl', 'en']
    
    for language in languages:
        sb_directory = Path(directory) / 'sb' / language
        version_file_path = get_highest_version_file(sb_directory)
        
        if version_file_path:
            # Load the OpenAPI spec file
            try:
                with open(version_file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(version_file_path, 'r', encoding='latin-1') as f:
                        file_content = f.read()
                except UnicodeDecodeError as e:
                    print(f"Error reading file {version_file_path}: {e}")
                    continue

            # Parse the JSON content
            endpointPathsContent = json.loads(file_content)
            
            # Ensure the 'paths' key exists in the OpenAPI spec
            if 'paths' in endpointPathsContent:
                paths = endpointPathsContent['paths']
                
                # Extract the method and endpoint from the 'paths' content
                for endpoint, methods in paths.items():
                    for method, details in methods.items():
                        # Ensure details is a dictionary
                        if isinstance(details, dict):
                            # create the path variable
                            # path example: https://docs.afas.help/apidoc/sb/nl/5-0-0#post-/app/token
                            path = f"apidoc/sb/{language}/{version_file_path.stem.replace('-', '.')}#{method}-{endpoint}"
                            cleanEndpoint = endpoint.replace('/', ' ')
                            # Create a JSON object with the extracted data and content
                            json_object_sb = {
                                'id': f"{version_file_path.stem}_{language}_{method}_{endpoint}".replace(' ', '_'),
                                'path': path,
                                'tags': details.get('tags', ''),
                                'language': language,
                                'product': 'sb',
                                'type': 'openapi',
                                'title': cleanEndpoint,
                                'content': f"{cleanEndpoint} {details.get('summary', '')}",
                                'category': '',
                                'version': '3.0.0',
                                'topic': ''
                            }

                            jsonl_data.append(json_object_sb)
            else:
                print(f"No 'paths' key found in the OpenAPI spec for {version_file_path}.")
        else:
            print(f"No valid version files found in {language} folder.")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                # make case insensitive
                file_name = file.lower()
                if file_name != 'endpointpaths.json':
                    continue
                
                file_path = Path(root) / file

                # load the Openapi spec file
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                except UnicodeDecodeError:
                    try:
                        with open(file_path, 'r', encoding='latin-1') as f:
                            file_content = f.read()
                    except UnicodeDecodeError as e:
                        print(f"Error reading file {file_path}: {e}")
                        continue

                # Parse the JSON content
                endpointPathsContent = json.loads(file_content)

                # Extract the method and endpoint from the openapi file content
                for endpoint, methods in endpointPathsContent.items():
                    for method, details in methods.items():
                        # Ensure details is a dictionary
                        product = 'Profit'

                        # Capitalize the method
                        capitalMethod = method.capitalize()

                        # create the content without leading and trailing slashes
                        contentEn = f"Endpoint: {endpoint}. Description: {details.get('descriptionEn', '')}. HTTP Method: {capitalMethod}".replace('/', ' ')
                        contentNl = f"Endpoint: {endpoint}. Beschrijving: {details.get('descriptionNl', '')}. HTTP Methode: {capitalMethod}".replace('/', ' ')
                        cleanEndpoint = f"{capitalMethod} {endpoint.replace('/', ' ')}"

                        if isinstance(details, dict):
                            # Create a JSON object with the extracted data and content
                            json_object_nl = {
                                'id': f"{file_path.stem}_en_{product}_{method}_{endpoint}".replace(' ', '_'),
                                'path': details.get('url', ''),
                                'topic': method,
                                'tags': [],
                                'language': "en",
                                'product': "Profit",
                                'type': 'openapi',
                                'title': cleanEndpoint,
                                'content': contentEn,
                                'category': '',
                                'version': '3.0.0'
                            }

                            jsonl_data.append(json_object_nl)

                            json_object_en = {
                                'id': f"{file_path.stem}_nl_{product}_{method}_{endpoint}".replace(' ', '_'),
                                'path': details.get('url', ''),
                                'topic': method,
                                'tags': [],
                                'language': "nl",
                                'product': "Profit",
                                'type': 'openapi',
                                'title': cleanEndpoint,
                                'content': contentNl,
                                'category': '',
                                'version': '3.0.0'
                            }

                            jsonl_data.append(json_object_en)

    return jsonl_data

def import_data_to_typesense(jsonl_data):
    try:
        result = client.collections[TYPESENSE_COLLECTION].documents.import_(jsonl_data, {'action': 'create'})
        print('Data imported successfully')
        print(result)
    except Exception as e:
        print('Error importing data to Typesense:', e)

def write_jsonl_to_file(jsonl_data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for json_line in jsonl_data:
            f.write(json.dumps(json_line) + '\n')

if __name__ == '__main__':

    extract_zip(zip_file_path, extracted_path)
    jsonl_data = read_openapi_files(extracted_path)

    # Import data to Typesense
    import_data_to_typesense(jsonl_data)