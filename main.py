from fastapi import FastAPI
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Elasticsearch credentials
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL")
ELASTICSEARCH_API_KEY = os.getenv("ELASTICSEARCH_API_KEY")

# Ensure environment variables are loaded correctly
if not ELASTICSEARCH_URL or not ELASTICSEARCH_API_KEY:
    raise ValueError("Missing Elasticsearch credentials in environment variables.")

# Connect to Elasticsearch
es = Elasticsearch(
    ELASTICSEARCH_URL,
    api_key=ELASTICSEARCH_API_KEY
)

# Initialize FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Search Engine is running!"}

@app.get("/search/")
def search(query: str):
    """Search Elasticsearch for matching documents."""
    search_query = {
        "query": {
            "match": {
                "name": query  # Adjust field name if needed
            }
        }
    }
    
    response = es.search(index="my_index", body=search_query)
    
    results = [
        {"id": hit["_id"], "name": hit["_source"]["name"], "sport": hit["_source"]["sport"]}
        for hit in response["hits"]["hits"]
    ]
    
    return {"results": results}
