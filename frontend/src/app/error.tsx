"use client";
export default function Error({ error }: { error: Error }) { return <main className="p-8"><h1 className="text-2xl text-magenta">Runtime boundary</h1><p>{error.message}</p></main>; }
