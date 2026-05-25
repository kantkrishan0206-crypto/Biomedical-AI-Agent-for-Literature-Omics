import { AgentGraphPanel } from "@/app/layout-sections/agent-graph-panel";
import { EvidencePanel } from "@/app/layout-sections/evidence-panel";
import { OmicsPanel } from "@/app/layout-sections/omics-panel";
import { TelemetryPanel } from "@/app/layout-sections/telemetry-panel";
import { AppShell } from "@/components/layout/app-shell";

export function WorkspaceShell() {
  return (
    <AppShell>
      <main className="grid flex-1 grid-cols-[360px_minmax(520px,1fr)_430px] gap-3 p-3">
        <AgentGraphPanel />
        <OmicsPanel />
        <div className="space-y-3"><TelemetryPanel /><EvidencePanel /></div>
      </main>
    </AppShell>
  );
}
