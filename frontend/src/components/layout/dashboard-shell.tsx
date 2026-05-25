import { AppShell } from "@/components/layout/app-shell";

export function DashboardShell({ title, children }: { title: string; children?: React.ReactNode }) {
  return (
    <AppShell>
      <main className="flex-1 p-6">
        <h1 className="mb-4 text-2xl font-semibold">{title}</h1>
        {children ?? <div className="cockpit-panel p-6 text-slate-300">Live research systems, workflow telemetry, provenance, and operational controls are available from this module.</div>}
      </main>
    </AppShell>
  );
}
