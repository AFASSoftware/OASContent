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

def drop_collection():
    try:
        client.collections[TYPESENSE_COLLECTION].delete()
        print('Collection dropped successfully')
    except Exception as e:
        print('Error dropping collection:', e)

if __name__ == '__main__':
    drop_collection()