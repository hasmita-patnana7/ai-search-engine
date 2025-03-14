from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get values from .env
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST")
ELASTICSEARCH_API_KEY = os.getenv("ELASTICSEARCH_API_KEY")

# Connect to Elasticsearch
es = Elasticsearch(ELASTICSEARCH_HOST, api_key=ELASTICSEARCH_API_KEY)

# Check connection
print(es.info())
