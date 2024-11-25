import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import QueryPage from "./pages/QueryPage";

function App() {
  const isAuthenticated = localStorage.getItem("authToken"); // Checa se o usuário está autenticado

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          path="/query"
          element={isAuthenticated ? <QueryPage /> : <Navigate to="/login" />}
        />
        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;
