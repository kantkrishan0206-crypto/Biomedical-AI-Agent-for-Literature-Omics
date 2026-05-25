"use client";
import { useEffect, useState } from "react";
export function usetelemetry() {
  const [state, setState] = useState({ status: "live" });
  useEffect(() => { const id = setInterval(() => setState({ status: "live", updatedAt: new Date().toISOString() } as any), 2000); return () => clearInterval(id); }, []);
  return state;
}
