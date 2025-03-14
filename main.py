from fastapi import FastAPI
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

# Initialize FastAPI
app = FastAPI()

# Define index name
INDEX_NAME = "search-index"

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Search API!"}

@app.get("/search/")
def search(query: str):
    """Search for documents in Elasticsearch."""
    search_query = {
        "query": {
            "match": {
                "content": query
            }
        }
    }
    
    response = es.search(index=INDEX_NAME, body=search_query)
    results = [
        {"title": hit["_source"]["title"], "content": hit["_source"]["content"]}
        for hit in response["hits"]["hits"]
    ]
    
    return {"results": results}
