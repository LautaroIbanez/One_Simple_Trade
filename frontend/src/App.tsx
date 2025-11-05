import { useState, useEffect } from "react";
import type { HealthResponse } from "../../shared/types/api";

function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/health")
      .then((res) => res.json())
      .then((data: HealthResponse) => {
        setHealth(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="app">
        <h1>One Simple Trade</h1>
        <p>Loading...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <h1>One Simple Trade</h1>
        <p className="error">Error: {error}</p>
        <p>Backend may not be running on port 8000</p>
      </div>
    );
  }

  return (
    <div className="app">
      <h1>One Simple Trade</h1>
      <div className="status">
        <p>Backend Status: {health?.status}</p>
        <p>Timestamp: {health?.timestamp ? new Date(health.timestamp).toISOString() : "N/A"}</p>
      </div>
      <p className="placeholder">
        Frontend scaffold functional. Signal display coming in Epic 2.
      </p>
    </div>
  );
}

export default App;

