# AI Search Engine

## 📌 Overview

This project is an AI-powered search engine that leverages Elasticsearch to index and retrieve data efficiently. It includes a Next.js frontend for the user interface, a web scraper for data collection, indexing scripts, and an API for querying the search engine.

## 🚀 Features

- 🔗 Connects to Elasticsearch for indexing and searching.
- 🌐 Includes a web scraper to gather data.
- 📡 API to query the search engine.
- ⚡ Efficient data indexing and retrieval.
- 🎨 User-friendly frontend built with Next.js.

## 🔧 Installation

### Backend Setup

1. Clone the repository:

   ```sh
    https://github.com/hasmita-patnana7/ai-search-engine.git
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Ensure Elasticsearch is running locally or provide a remote instance.

4. Start by indexing data:

   ```sh
   python index_data.py
   ```

5. Run the search API:

   ```sh
   python search_api.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install frontend dependencies:
   ```sh
   npm install
   ```
3. Start the frontend application:
   ```sh
   npm run dev
   ```
4. Open your browser and visit:
   ```sh
   http://localhost:3000
   ```

## 📂 Project Structure

### Backend

- 📜 `main.py` - Main script to run the search engine.
- 🔌 `connect_elasticsearch.py` - Handles Elasticsearch connections.
- 📊 `index_data.py` - Indexes data into Elasticsearch.
- 🕷️ `scraper.py` - Collects data from web sources.
- 🔍 `search_api.py` - Provides an API interface for search queries.
- 📌 `search_data.py` - Manages search-related operations.
- 📦 `requirements.txt` - Lists required dependencies.

### Frontend

- 📁 `frontend/pages/` - Contains Next.js pages.
  - `index.js` - Main search interface.
  - `_app.js` and `_document.js` - Next.js configuration files.
  - `api/hello.js` - Example API route.
- 🎨 `frontend/styles/globals.css` - Global styles for the application.

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

## 🤝 Contributing

Feel free to open issues or submit pull requests to enhance the project!

## 📧 Contact

For any inquiries, contact [your email or GitHub profile].

