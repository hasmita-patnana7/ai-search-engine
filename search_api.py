from fastapi import FastAPI
from elasticsearch import Elasticsearch
import json

app = FastAPI()
es = Elasticsearch("http://localhost:9200")

@app.get("/search/")
def search(query: str):
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content"],
                "fuzziness": "AUTO"
            }
        }
    }

    try:
        results = es.search(index="wikipedia_articles", body=search_body)

        # 🔍 Debugging: Print the raw Elasticsearch response
        print("\n==== Elasticsearch Response ====")
        print(json.dumps(results, indent=2))

        hits = results["hits"]["hits"]

        if not hits:
            print("⚠ No matching results found!")

        return {"results": [
            {
                "title": hit["_source"].get("title", "No Title"),
                "content": hit["_source"].get("content", "No Content")
            } 
            for hit in hits
        ]}

    except Exception as e:
        print("🚨 FastAPI Error:", str(e))
        return {"error": str(e)}
