"use client";
const cards = [["A100",72,"7 / 10"],["H100",63,"5 / 8"],["L40S",45,"3 / 6"],["TPU v5e",38,"2 / 4"]];

export function TelemetryPanel() {
  return (
    <section className="cockpit-panel p-4">
      <div className="mb-4 flex justify-between"><h2 className="text-sm font-semibold uppercase">Infrastructure Telemetry</h2><span className="text-xs text-mint">Live</span></div>
      <div className="mb-5 grid grid-cols-4 gap-2">
        {cards.map(([name, value, jobs]) => <div key={name as string} className="rounded-md border border-line p-3 text-center"><div className="text-xs text-slate-400">{name}</div><div className="mx-auto my-3 grid h-16 w-16 place-items-center rounded-full border-4 border-mint text-lg font-semibold text-mint">{value}%</div><div className="text-xs text-slate-300">{jobs} Jobs</div></div>)}
      </div>
      <div className="rounded-md border border-line p-3">
        <div className="mb-2 text-xs uppercase">Cluster Utilization</div>
        <svg viewBox="0 0 420 120" className="h-32 w-full">
          {["#12dff3","#0ea5e9","#ff2fa3","#fbbf24"].map((color, row) => <polyline key={color} points={Array.from({ length: 40 }, (_, i) => `${i*11},${70 + Math.sin(i/2 + row)*18 + row*4}`).join(" ")} fill="none" stroke={color} strokeWidth="2" />)}
        </svg>
      </div>
      <div className="mt-4 rounded-md border border-line p-3">
        <div className="mb-3 flex justify-between text-xs uppercase"><span>Vector Database - Streaming Indexing</span><span className="text-mint">Live</span></div>
        <div className="grid grid-cols-4 gap-2 text-center text-xs">{[["Indexing Rate","12,842 /min"],["Vectors","482.7M"],["Queue Length","21,731"],["Recall@10","0.96"]].map(([k,v]) => <div key={k} className="rounded border border-line p-2"><div className="text-slate-400">{k}</div><div className="text-base text-mint">{v}</div></div>)}</div>
        <div className="mt-3 space-y-2 text-xs text-slate-300">{["Indexed 1,246 vectors PMIDs: 39876261-39877506","Linked 842 entities to knowledge graph","Batch commit successful (3.2s)"].map((log) => <div key={log}>- {log}</div>)}</div>
      </div>
    </section>
  );
}
