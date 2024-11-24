import React, { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState(null);
  const [error, setError] = useState("");

  const handleQuerySubmit = async () => {
    try {
      setError("");
      const response = await axios.post("http://127.0.0.1:8000/query", { query });
      setResults(response.data.results);
    } catch (err) {
      setError(err.response?.data?.detail || "Erro ao executar a consulta");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Consulta PostgreSQL</h1>
      <textarea
        rows="5"
        cols="50"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Digite sua consulta SQL aqui..."
      />
      <br />
      <button onClick={handleQuerySubmit}>Executar Consulta</button>
      <div style={{ marginTop: "20px" }}>
        {error && <p style={{ color: "red" }}>Erro: {error}</p>}
        {results && (
          <pre
            style={{
              background: "#f4f4f4",
              padding: "10px",
              borderRadius: "5px",
            }}
          >
            {JSON.stringify(results, null, 2)}
          </pre>
        )}
      </div>
    </div>
  );
}

export default App;
