import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")
index_name = "wikipedia_articles"

# Function to scrape Wikipedia
def scrape_wikipedia(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None  # Return None if page not found

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    content = ' '.join([p.text for p in paragraphs[:5]])  # First 5 paragraphs
    
    return {"title": topic, "content": content}

# Function to store in Elasticsearch
def store_in_elasticsearch(topic):
    data = scrape_wikipedia(topic)
    
    if data:
        es.index(index=index_name, body=data)
        print(f"✅ Stored {topic} in Elasticsearch!")
    else:
        print(f"❌ Failed to scrape {topic}")

# Example Usage
if __name__ == "__main__":
    topics = ["Artificial Intelligence", "Machine Learning", "Deep Learning"]
    for topic in topics:
        store_in_elasticsearch(topic)
