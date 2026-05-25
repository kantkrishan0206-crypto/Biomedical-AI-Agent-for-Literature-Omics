"use client";
import { create } from "zustand";
export const useTelemetryStore = create(() => ({ status: "ready" }));
