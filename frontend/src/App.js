import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import QueryPage from "./pages/QueryPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/query" element={<QueryPage />} />
        <Route path="*" element={<Navigate to="/query" />} />
      </Routes>
    </Router>
  );
}

export default App;
