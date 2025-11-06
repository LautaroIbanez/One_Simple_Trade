import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "./App";

// Mock fetch
global.fetch = async () =>
  ({
    json: async () => ({
      status: "ok",
      timestamp: 1234567890,
    }),
  }) as Response;

describe("App", () => {
  it("renders the app title", async () => {
    render(<App />);
    const title = await screen.findByText("One Simple Trade");
    expect(title).toBeDefined();
  });

  it("displays backend status after loading", async () => {
    render(<App />);
    const status = await screen.findByText(/Backend Status:/);
    expect(status).toBeDefined();
  });
});


