import { describe, it, expect, beforeEach, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "./App";

const mockSignal = {
  asset: "BTC",
  quote: "USD",
  timeframe: "1d",
  signal: "BUY",
  confidence: 0.73,
  explanation: "Bullish momentum",
  model_version: "1.0.0",
  as_of_utc: 1_700_000_000_000,
  latency_ms: 42,
  indicators_snapshot: {
    timestamp: 1_700_000_000_000,
    close: 50000,
  },
  disclaimer: "Not financial advice",
  methodology_url: "https://example.com",
};

describe("App", () => {
  beforeEach(() => {
    vi.spyOn(global, "fetch").mockResolvedValue({
      json: async () => mockSignal,
    } as Response);
  });

  it("renders the app title", async () => {
    render(<App />);
    const title = await screen.findByText("One Simple Trade");
    expect(title).toBeDefined();
  });

  it("renders signal, confidence and timestamp from /v1/signal", async () => {
    render(<App />);
    const signalEl = await screen.findByTestId("signal-value");
    const confidenceEl = await screen.findByTestId("confidence-value");
    const asOfEl = await screen.findByTestId("asof-value");

    expect(signalEl.textContent).toBe("BUY");
    expect(confidenceEl.textContent).toBe("73%");
    expect(asOfEl.textContent).toBe(new Date(mockSignal.as_of_utc).toISOString());
  });
});


