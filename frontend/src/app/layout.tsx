import type { Metadata } from "next";
import { Providers } from "@/app/providers";
import "./globals.css";
import "@/styles/animations.css";
import "@/styles/themes.css";

export const metadata: Metadata = {
  title: "Biomedical AI Agent for Literature + Omics",
  description: "Research-grade biomedical AI systems engineering platform"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
