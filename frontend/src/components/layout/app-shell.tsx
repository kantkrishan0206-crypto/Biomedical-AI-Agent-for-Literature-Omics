import { Sidebar } from "@/app/layout-sections/sidebar";
import { Topbar } from "@/app/layout-sections/topbar";

export function AppShell({ children }: { children: React.ReactNode }) {
  return <div className="min-h-screen bg-cockpit"><Topbar /><div className="flex min-h-[calc(100vh-4rem)]"><Sidebar />{children}</div></div>;
}
