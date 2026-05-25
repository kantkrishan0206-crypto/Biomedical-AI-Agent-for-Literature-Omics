import { cn } from "@/lib/utils";
export function Input(props: React.InputHTMLAttributes<HTMLInputElement>) { return <input {...props} className={cn("rounded-md border border-line bg-[#071017] px-3 py-2 text-sm", props.className)} />; }
