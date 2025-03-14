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

# Search query
query = {
    "query": {
        "match": {
            "content": "FastAPI"
        }
    }
}

# Perform the search
response = es.search(index=INDEX_NAME, body=query)

# Print results
for hit in response["hits"]["hits"]:
    print(f"Title: {hit['_source']['title']}")
    print(f"Content: {hit['_source']['content']}")
    print("-" * 50)
