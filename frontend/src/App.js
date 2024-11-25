import React, { useState, useEffect } from "react";
import axios from "axios";
import PropTypes from "prop-types";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleQuerySubmit = async () => {
    setLoading(true);
    setError("");
    setResults(null);
    try {
      const response = await axios.post("http://127.0.0.1:8000/query", { query });
      setResults(response.data.results);
    } catch (err) {
      setError(err.response?.data?.detail || "Erro ao executar a consulta");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (error) {
      console.error("Query error:", error);
    }
  }, [error]);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white p-6 rounded-lg shadow-md w-full max-w-2xl">
        <h1 className="text-3xl font-semibold text-center text-blue-600 mb-6">
          Aura Serverless - Query Executor
        </h1>
        <textarea
          rows="5"
          className="w-full p-3 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Digite sua consulta SQL aqui..."
        />
        <div className="text-center">
          <button
            onClick={handleQuerySubmit}
            className="bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            disabled={loading}
          >
            {loading ? "Executando..." : "Executar Consulta"}
          </button>
        </div>
        <div className="mt-6">
          {error && (
            <p className="text-red-500 text-center">{error}</p>
          )}
          {results && (
            <pre className="bg-gray-800 text-white p-4 rounded-lg mt-4">
              {JSON.stringify(results, null, 2)}
            </pre>
          )}
        </div>
      </div>
    </div>
  );
}

App.propTypes = {
  query: PropTypes.string,
  results: PropTypes.object,
  error: PropTypes.string,
  loading: PropTypes.bool,
};

export default App;
