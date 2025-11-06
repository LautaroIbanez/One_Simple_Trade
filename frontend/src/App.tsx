import { useState, useEffect } from "react";
import type { SignalResponse } from "../../shared/types/api";

function App() {
  const [signal, setSignal] = useState<SignalResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/v1/signal")
      .then((res) => res.json())
      .then((data: SignalResponse) => {
        setSignal(data);
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
      <section className="signal-card">
        <h2>Daily Signal</h2>
        <p>
          Signal: <strong data-testid="signal-value">{signal?.signal ?? "-"}</strong>
        </p>
        <p>
          Confidence: <span data-testid="confidence-value">{signal ? `${Math.round(signal.confidence * 100)}%` : "-"}</span>
        </p>
        <p>
          As of: <time data-testid="asof-value">{signal ? new Date(signal.as_of_utc).toISOString() : "-"}</time>
        </p>
      </section>
      <p className="placeholder">Scaffold listo. Layout base para Epic 2.</p>
    </div>
  );
}

export default App;


