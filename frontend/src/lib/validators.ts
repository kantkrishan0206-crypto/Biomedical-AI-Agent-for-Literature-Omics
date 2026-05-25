export function assertNonEmpty(value: string, field: string) {
  if (!value.trim()) throw new Error(`${field} is required`);
}
