export type Json = string | number | boolean | null | Json[] | { [key: string]: Json };
export type ApiRecord = { id: string; status: string; data?: Record<string, Json> };
