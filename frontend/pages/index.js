import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const search = async () => {
    if (!query) return;
    try {
      const response = await axios.get(
        `https://ai-search-engine-hprr.onrender.com/search/?query=${query}`
      );
      setResults(response.data.results || []);
    } catch (error) {
      console.error("Search error:", error);
    }
  };

  return (
    <div className="flex flex-col items-center p-10">
      <h1 className="text-3xl font-bold mb-4">AI Search Engine</h1>
      <input
        type="text"
        placeholder="Search..."
        className="border px-3 py-2 w-80 rounded-lg"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={search} className="mt-3 px-4 py-2 bg-blue-500 text-white rounded">
        Search
      </button>

      <div className="mt-6 w-full max-w-2xl">
        {results.length > 0 ? (
          results.map((res, index) => (
            <div key={index} className="border p-4 my-2 rounded shadow">
              <h2 className="text-lg font-semibold">{res.title}</h2>
              <p className="text-sm">{res.content.substring(0, 200)}...</p>
            </div>
          ))
        ) : (
          <p className="text-gray-500">No results found.</p>
        )}
      </div>
    </div>
  );
}
