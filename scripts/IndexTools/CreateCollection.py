import os
from typesense import Client
from dotenv import load_dotenv

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

def create_collection():
    schema = {
        'name': TYPESENSE_COLLECTION,
        'fields': [
            {'name': 'id', 'type': 'string'},  # Id
            {'name': 'topic', 'type': 'string'},  # Endpoint (Markdown) or API Endpoint (OpenAPI)
            {'name': 'title', 'type': 'string'},  # Title (Markdown)
            {'name': 'content', 'type': 'string'},  # Content (Markdown) or API Content (OpenAPI)
            {'name': 'language', 'type': 'string', 'facet': True},  # Language
            {'name': 'category', 'type': 'string'},  # Category (Markdown)
            {'name': 'path', 'type': 'string'},  # File Path (Markdown)
            {'name': 'product', 'type': 'string', 'facet': True},  # Product
            {'name': 'type', 'type': 'string', 'facet': True},  # Type (Markdown or OpenAPI)
            {'name': 'tags', 'type': 'string[]', 'facet': True},  # Tags (Markdown)
            {'name': 'version', 'type': 'string'},  # Version (OpenAPI)
        ]
    }

    try:
        client.collections.create(schema)
        print('Collection created successfully')
    except Exception as e:
        print('Error creating collection:', e)

if __name__ == '__main__':
    create_collection()