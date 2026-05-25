"use client";
import { QueryClient } from "@tanstack/react-query";
export const queryClient = new QueryClient({ defaultOptions: { queries: { refetchInterval: 15000, staleTime: 5000 } } });
