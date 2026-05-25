import { env } from "@/lib/env";

export function agentWebSocket() {
  const url = env.apiBaseUrl.replace("http", "ws") + "/api/v1/agents/ws";
  return new WebSocket(url);
}
