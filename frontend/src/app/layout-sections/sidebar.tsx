import { Activity, BookOpen, Boxes, Brain, CircleDot, Database, FlaskConical, GitBranch, HardDrive, Network, Settings, Workflow } from "lucide-react";
import { sideNav } from "@/lib/constants";

const icons = [Activity, BookOpen, Brain, CircleDot, GitBranch, FlaskConical, Database, Boxes, Workflow, HardDrive, Network, Settings];

export function Sidebar() {
  let i = 0;
  return (
    <aside className="flex w-36 shrink-0 flex-col border-r border-line bg-[#071017]/95 text-sm">
      <div className="flex-1 space-y-6 overflow-y-auto px-3 py-5 thin-scrollbar">
        {Object.entries(sideNav).map(([section, items]) => (
          <div key={section}>
            <div className="mb-3 text-[11px] uppercase text-slate-500">{section}</div>
            <div className="space-y-2">
              {items.map((item) => {
                const Icon = icons[i++ % icons.length];
                return <a key={item} href="#" className="flex items-center gap-2 rounded-md px-2 py-2 text-slate-300 hover:bg-cyan/10 hover:text-cyan"><Icon size={15} />{item}</a>;
              })}
            </div>
          </div>
        ))}
      </div>
      <div className="border-t border-line p-3 text-xs text-slate-400">
        <div className="mb-2 flex items-center gap-2"><Settings size={14} /> Settings</div>
        <div className="rounded border border-mint/40 bg-mint/10 p-2 text-mint">All Systems Operational</div>
      </div>
    </aside>
  );
}
