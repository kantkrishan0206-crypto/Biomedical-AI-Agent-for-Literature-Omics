import { Bell, HelpCircle, Search } from "lucide-react";
import { topNav } from "@/lib/constants";

export function Topbar() {
  return (
    <header className="flex h-16 items-center border-b border-line bg-[#050b11]/90 px-5">
      <div className="flex min-w-72 items-center gap-3">
        <img src="/logo.svg" alt="" className="h-9 w-9" />
        <div>
          <div className="text-xl font-semibold">OMICS Codex</div>
          <div className="text-xs text-slate-400">AI for Accelerated Science</div>
        </div>
      </div>
      <nav className="flex flex-1 justify-center gap-8 text-sm text-slate-300">
        {topNav.map((item) => <a key={item} className={item === "Workbench" ? "border-b-2 border-mint px-1 py-5 text-white" : "py-5"} href={"/" + item.toLowerCase().replaceAll(" ", "-")}>{item}</a>)}
      </nav>
      <div className="flex items-center gap-3">
        <div className="hidden h-9 items-center gap-2 rounded-md border border-line px-3 text-sm text-slate-400 lg:flex"><Search size={16} /> Search <span className="ml-16">Ctrl+K</span></div>
        <button className="rounded-md border border-line p-2"><Bell size={16} /></button>
        <button className="rounded-md border border-line p-2"><HelpCircle size={16} /></button>
        <div className="grid h-9 w-9 place-items-center rounded-full border border-mint text-sm text-mint">KK</div>
      </div>
    </header>
  );
}
