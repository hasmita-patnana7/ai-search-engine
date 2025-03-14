from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to Elasticsearch
es = Elasticsearch(
    os.getenv("ELASTICSEARCH_HOST"),
    api_key=os.getenv("ELASTICSEARCH_API_KEY")
)

# Define the index name
INDEX_NAME = "search-index"

# Create an index (if it doesn't exist)
if not es.indices.exists(index=INDEX_NAME):
    es.indices.create(index=INDEX_NAME)
    print(f"Index '{INDEX_NAME}' created successfully.")

# Sample data to index
documents = [
    {"id": 1, "title": "Elasticsearch Guide", "content": "Learn how to use Elasticsearch for full-text search."},
    {"id": 2, "title": "FastAPI Tutorial", "content": "A beginner's guide to FastAPI for building APIs."},
    {"id": 3, "title": "Machine Learning Basics", "content": "Introduction to ML concepts and algorithms."},
]

# Insert data into the index
for doc in documents:
    es.index(index=INDEX_NAME, id=doc["id"], document=doc)

print("Data indexed successfully!")
