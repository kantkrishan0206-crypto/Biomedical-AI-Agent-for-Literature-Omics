import Link from "next/link";
export default function AuthPage() {
  return <main className="grid min-h-screen place-items-center p-6"><section className="cockpit-panel w-full max-w-md p-6"><h1 className="mb-2 text-2xl font-semibold">forgot password</h1><p className="mb-4 text-sm text-slate-400">Secure research workspace access for kantkrishan0206@gmail.com ownership and team use.</p><input aria-label="email" className="mb-3 w-full rounded border border-line bg-[#071017] p-3" /><input aria-label="password" className="mb-4 w-full rounded border border-line bg-[#071017] p-3" type="password" /><Link className="block rounded bg-mint px-4 py-3 text-center font-semibold text-black" href="/workbench">Continue</Link></section></main>;
}
