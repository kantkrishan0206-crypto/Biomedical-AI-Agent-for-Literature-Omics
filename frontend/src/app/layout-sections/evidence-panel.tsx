import { evidence } from "@/lib/constants";

export function EvidencePanel() {
  return (
    <section className="cockpit-panel p-4">
      <h2 className="mb-4 text-sm font-semibold uppercase">Citation-Grounded Evidence</h2>
      <div className="mb-3 flex gap-6 border-b border-line text-xs text-slate-400"><span className="border-b-2 border-cyan pb-2 text-cyan">Top Evidence</span><span>Mechanistic Insights</span><span>Clinical Evidence</span></div>
      <div className="space-y-3">
        {evidence.map((item, index) => <article key={item.pmid} className="rounded-md border border-line bg-[#071017]/80 p-3">
          <div className="flex gap-3"><span className="grid h-7 w-7 shrink-0 place-items-center rounded bg-slate-800 text-sm">{index + 1}</span><div><h3 className="text-sm font-semibold">{item.title}</h3><p className="text-xs text-slate-400">PMID: {item.pmid} - {item.journal} - {item.year}</p><p className="mt-2 text-xs text-slate-300">Evidence supports SMN2-centered therapeutic hypotheses with reproducible citation provenance.</p></div><span className="ml-auto h-fit rounded bg-mint/20 px-2 py-1 text-xs text-mint">Supports {item.supports}</span></div>
        </article>)}
      </div>
    </section>
  );
}
