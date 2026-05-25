"use client";
import { Maximize2, RotateCcw, SlidersHorizontal } from "lucide-react";
import { clusterColors, clusters } from "@/lib/constants";

function points() {
  return Array.from({ length: 720 }, (_, i) => {
    const cluster = i % clusters.length;
    const angle = i * 0.43 + cluster;
    const radius = 90 + cluster * 13 + Math.sin(i) * 12;
    return { x: 260 + Math.cos(angle) * radius + (cluster % 3) * 20, y: 170 + Math.sin(angle) * radius + Math.floor(cluster / 3) * 18, cluster };
  });
}

export function OmicsPanel() {
  return (
    <section className="space-y-3">
      <div className="cockpit-panel p-4">
        <div className="mb-3 flex items-center justify-between"><h2 className="text-sm font-semibold uppercase">Single-cell RNA-seq - Human Motor Neuron Dataset</h2><div className="flex items-center gap-3 text-xs text-slate-300">Cluster Resolution <input type="range" defaultValue="80" /> <span className="rounded border border-line px-2 py-1">0.8</span></div></div>
        <div className="grid grid-cols-[1fr_220px] gap-4">
          <div className="relative min-h-[390px]">
            <div className="absolute left-0 top-0 z-10 flex flex-col gap-2 rounded-md border border-line bg-[#071017]/80 p-2"><SlidersHorizontal size={16} /><Maximize2 size={16} /><RotateCcw size={16} /></div>
            <svg viewBox="0 0 560 390" className="h-full w-full">
              <line x1="70" y1="340" x2="520" y2="340" stroke="#244655" /><line x1="70" y1="30" x2="70" y2="340" stroke="#244655" />
              {points().map((p, i) => <circle key={i} cx={p.x} cy={p.y} r="2.2" fill={clusterColors[p.cluster]} opacity=".9" />)}
              <text x="260" y="372" fill="#9fb6c2" fontSize="13">UMAP_1</text><text x="18" y="190" fill="#9fb6c2" fontSize="13" transform="rotate(-90 18 190)">UMAP_2</text>
            </svg>
          </div>
          <div className="rounded-md border border-line p-3">
            {clusters.map((cluster, i) => <div key={cluster} className="mb-3 flex items-center justify-between text-xs"><span className="flex items-center gap-2"><span className="h-3 w-3 rounded" style={{ background: clusterColors[i] }} />{i} {cluster}</span><span>{[1847,1562,1276,2341,1105,1002,892,645,713][i].toLocaleString()}</span></div>)}
            <div className="mt-5 border-t border-line pt-3 text-xs text-slate-300"><div>Total Cells <span className="float-right">11,804</span></div><div>Genes <span className="float-right">24,311</span></div></div>
          </div>
        </div>
      </div>
      <div className="cockpit-panel grid min-h-[320px] grid-cols-[120px_1fr_140px] gap-4 p-4">
        <div className="text-sm text-slate-300"><h3 className="mb-4 text-xs font-semibold uppercase text-white">3D Molecular Viewer - Drug-Target Interaction</h3>{["Target SMN2", "PDB ID 7JQ5", "Resolution 2.40 A", "Ligand OCX-101", "Affinity -9.2 kcal/mol"].map((x) => <div key={x} className="border-b border-line py-3">{x}</div>)}</div>
        <svg viewBox="0 0 640 320" className="h-full w-full rounded-md bg-[#07121b]">
          <defs><filter id="blur"><feGaussianBlur stdDeviation="7"/></filter></defs>
          {Array.from({ length: 34 }, (_, i) => <circle key={i} cx={80 + (i * 37) % 500} cy={40 + (i * 53) % 240} r="38" fill="#24486b" opacity=".35" filter="url(#blur)" />)}
          <polyline points="110,180 170,150 235,172 300,126 370,154 450,130 520,180" fill="none" stroke="#20f29a" strokeWidth="7" strokeLinecap="round" />
          <polyline points="120,70 190,105 250,80 330,98 410,70 500,112" fill="none" stroke="#7aa7ff" strokeWidth="5" opacity=".75" />
          {["Tyr234", "Gln269", "Lys190"].map((label, i) => <text key={label} x={280 + i * 110} y={125 + i * 62} fill="#fff" fontSize="16">{label}</text>)}
        </svg>
        <div className="space-y-4 text-xs"><div className="rounded-md border border-line p-3">{["Hydrogen Bond","Hydrophobic","pi-pi Stacking","Salt Bridge"].map((x) => <label key={x} className="mb-2 flex gap-2"><input type="checkbox" defaultChecked /> {x}</label>)}</div><div className="rounded-md border border-line p-3">Opacity <input className="w-full" type="range" defaultValue="60" /></div></div>
      </div>
    </section>
  );
}
