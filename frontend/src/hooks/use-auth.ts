"use client";
import { devSession } from "@/lib/auth";
export function useAuth() { return { session: devSession(), hasRole: (role: string) => devSession().role === role }; }
