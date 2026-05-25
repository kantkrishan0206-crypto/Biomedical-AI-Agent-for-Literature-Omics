export type Session = { email: string; role: "admin" | "researcher" | "viewer" };

export function devSession(): Session {
  return { email: "kantkrishan0206@gmail.com", role: "admin" };
}
