/**
 * Shared TypeScript types for API contracts between frontend and backend.
 */

export type Signal = "BUY" | "HOLD" | "SELL";

export interface IndicatorPoint {
  timestamp: number;
  close: number;
  ema_fast?: number | null;
  ema_slow?: number | null;
  rsi?: number | null;
  macd?: number | null;
  macd_signal?: number | null;
  atr?: number | null;
  vol_30d?: number | null;
}

export interface MarketOhlcResponse {
  asset: string;
  quote: string;
  timeframe: string;
  source: string;
  latency_ms: number;
  as_of_utc: number;
  candles: IndicatorPoint[];
}

export interface SignalResponse {
  asset: string;
  quote: string;
  timeframe: string;
  signal: Signal;
  confidence: number;
  explanation: string;
  model_version: string;
  as_of_utc: number;
  latency_ms: number;
  indicators_snapshot: IndicatorPoint;
  disclaimer: string;
  methodology_url: string;
}

export interface HealthResponse {
  status: string;
  timestamp: number;
}

