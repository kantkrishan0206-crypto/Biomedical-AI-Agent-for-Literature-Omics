import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        cockpit: "#071017",
        panel: "#0a1720",
        line: "#183241",
        cyan: "#12dff3",
        mint: "#20f29a",
        violet: "#a855f7",
        magenta: "#ff2fa3",
        amber: "#fbbf24"
      },
      borderRadius: {
        panel: "8px"
      }
    }
  },
  plugins: []
};
export default config;
