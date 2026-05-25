"use client";
import { Brain, Database, FileSearch, Network, ShieldCheck, Sparkles } from "lucide-react";

const nodes = [
  { id: "User Query", x: 38, y: 5, c: "border-mint", icon: Sparkles, detail: "What drives SMA pathogenesis?" },
  { id: "Orchestrator Agent", x: 34, y: 24, c: "border-cyan", icon: Brain, detail: "12.4k tokens" },
  { id: "Literature Agent", x: 8, y: 42, c: "border-mint", icon: FileSearch, detail: "12,842 papers" },
  { id: "KG Agent", x: 64, y: 42, c: "border-cyan", icon: Network, detail: "87,731 nodes" },
  { id: "Evidence Agent", x: 8, y: 61, c: "border-sky-400", icon: ShieldCheck, detail: "9,215 claims" },
  { id: "Data Agent", x: 64, y: 61, c: "border-violet", icon: Database, detail: "37 datasets" },
  { id: "Hypothesis Agent", x: 35, y: 78, c: "border-magenta", icon: Brain, detail: "37 hypotheses" },
  { id: "Answer Synthesis Agent", x: 32, y: 93, c: "border-mint", icon: Sparkles, detail: "confidence 0.92" }
];

export function AgentGraphPanel() {
  return (
    <section className="cockpit-panel grid-bg relative min-h-[680px] overflow-hidden p-4">
      <div className="mb-3 flex items-start justify-between">
        <div><h2 className="text-sm font-semibold uppercase">Agent Reasoning Graph</h2><p className="text-xs text-slate-400">Live Multi-Agent Reasoning (LangGraph)</p></div>
        <div className="text-xs text-mint">LIVE</div>
      </div>
      <svg className="absolute inset-0 mt-16 h-[560px] w-full" viewBox="0 0 100 100" preserveAspectRatio="none">
        {[[0,1],[1,2],[1,3],[2,4],[3,5],[4,6],[5,6],[6,7]].map(([a,b]) => <path key={a + '-' + b} d={`M ${nodes[a].x+10} ${nodes[a].y+5} C 50 ${nodes[a].y+10}, 50 ${nodes[b].y-5}, ${nodes[b].x+10} ${nodes[b].y}`} stroke="#12dff3" strokeDasharray="1 1" fill="none" opacity=".75" />)}
      </svg>
      {nodes.map((node) => {
        const Icon = node.icon;
        return <div key={node.id} className={`absolute w-40 rounded-md border bg-[#071017]/90 p-3 text-xs shadow-xl ${node.c}`} style={{ left: node.x + "%", top: node.y + "%" }}>
          <div className="mb-1 flex items-center gap-2 font-semibold"><Icon size={14} /> {node.id}</div>
          <div className="text-slate-400">{node.detail}</div>
        </div>;
      })}
      <div className="absolute bottom-4 left-4 right-4 grid grid-cols-4 gap-2 rounded-md border border-line bg-[#061018]/95 p-3 text-center">
        {["7 / 7 Agents", "1.24M Tokens", "2,431 Steps", "00:04:32 Wall Time"].map((metric) => <div key={metric} className="border-r border-line last:border-r-0"><div className="text-lg text-white">{metric.split(" ")[0]}</div><div className="text-[11px] text-slate-400">{metric.replace(metric.split(" ")[0], "")}</div></div>)}
      </div>
    </section>
  );
}
