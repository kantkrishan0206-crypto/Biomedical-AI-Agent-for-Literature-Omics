import { cn } from "@/lib/utils";
export function Button({ className, ...props }: React.ButtonHTMLAttributes<HTMLButtonElement>) { return <button className={cn("rounded-md border border-line px-3 py-2 text-sm hover:border-cyan hover:text-cyan", className)} {...props} />; }
