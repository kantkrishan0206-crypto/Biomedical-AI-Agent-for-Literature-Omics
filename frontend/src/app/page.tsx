import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen p-8">
      <section className="mx-auto flex min-h-[calc(100vh-4rem)] max-w-7xl flex-col justify-between">
        <div className="pt-20">
          <p className="text-sm uppercase tracking-[.22em] text-cyan">Research-Grade Biomedical AI Systems Engineering Platform</p>
          <h1 className="mt-5 max-w-4xl text-6xl font-semibold leading-tight">Biomedical AI Agent for Literature + Omics</h1>
          <p className="mt-6 max-w-2xl text-lg text-slate-300">Autonomous biomedical literature reasoning, omics interpretation, knowledge graph traversal, workflow DAG execution, provenance, and production telemetry in one scientific cockpit.</p>
          <Link href="/workbench" className="mt-8 inline-flex rounded-md border border-cyan/60 bg-cyan/10 px-5 py-3 text-sm font-medium text-cyan">Open Workbench</Link>
        </div>
        <div className="cockpit-panel grid grid-cols-4 gap-4 p-4 text-sm text-slate-300">
          {["Agent Graph", "Qdrant Retrieval", "Workflow DAGs", "Ollama Inference"].map((item) => <div key={item} className="rounded-md border border-line p-4">{item}</div>)}
        </div>
      </section>
    </main>
  );
}
