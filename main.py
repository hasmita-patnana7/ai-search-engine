from fastapi import FastAPI
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

# ✅ Initialize FastAPI before defining routes
app = FastAPI()

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

@app.get("/")
def read_root():
    return {"message": "AI Search Engine is running!"}

@app.get("/search/")
def search(query: str):
    """Search Elasticsearch for matching documents."""
    try:
        search_query = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "content"],
                    "fuzziness": "AUTO"
                }
            }
        }
        
        response = es.search(index="wikipedia_articles", body=search_query)
        print("Elasticsearch Response:", response)  # DEBUG
        
        results = [
            {"title": hit["_source"]["title"], "content": hit["_source"]["content"]}
            for hit in response["hits"]["hits"]
        ]
        
        return {"results": results}

    except Exception as e:
        print("Error:", e)  # DEBUG
        return {"error": str(e)}
