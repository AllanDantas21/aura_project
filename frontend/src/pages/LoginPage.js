import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function LoginPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        setError("");
        if (!username || !password) {
            setError("Todos os campos são obrigatórios!");
            return;
        }
        setLoading(true);
        if (username === "admin" && password === "123") {
            localStorage.setItem("authToken", "authenticated");
            navigate("/query");
        } else {
            setError("Credenciais inválidas!");
        }
        setLoading(false);
    };

    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
            <div className="w-full max-w-md bg-white p-6 rounded-lg shadow-md">
                <h1 className="text-2xl font-bold mb-4 text-center">Login</h1>
                {error && <p className="text-red-500">{error}</p>}
                <form onSubmit={handleLogin}>
                    <div className="mb-4">
                        <label htmlFor="username" className="block mb-2">Usuário</label>
                        <input
                            type="text"
                            id="username"
                            placeholder="Usuário"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            className="w-full p-2 border border-gray-300 rounded-md"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="password" className="block mb-2">Senha</label>
                        <input
                            type="password"
                            id="password"
                            placeholder="Senha"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full p-2 border border-gray-300 rounded-md"
                        />
                    </div>
                    <button
                        type="submit"
                        disabled={loading}
                        className={`w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 ${loading ? "opacity-50 cursor-not-allowed" : ""}`}
                    >
                        {loading ? "Entrando..." : "Entrar"}
                    </button>
                </form>
            </div>
        </div>
    );
}

export default LoginPage;
