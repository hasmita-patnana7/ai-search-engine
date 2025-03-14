from fastapi import FastAPI
from elasticsearch import Elasticsearch

app = FastAPI()
es = Elasticsearch("http://localhost:9200")
index_name = "wikipedia_articles"

@app.get("/search/")
def search(query: str):
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content"]
            }
        }
    }
    results = es.search(index=index_name, body=search_body)
    hits = results["hits"]["hits"]
    
    return {"results": [{"title": hit["_source"]["title"], "content": hit["_source"]["content"]} for hit in hits]}


