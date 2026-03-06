import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { Syne, DM_Sans } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

const syne = Syne({ subsets: ["latin"], weight: ["700", "800"], variable: "--tm-font-display" });
const dmSans = DM_Sans({ subsets: ["latin"], weight: ["300", "400", "500", "600"], variable: "--tm-font" });

export const metadata: Metadata = {
  title: "TM Relatório - Premium Tool",
  description: "Gerador de Relatório Fotográfico Inteligente",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR" className={`${syne.variable} ${dmSans.variable}`}>
      <body className={`antialiased min-h-screen`} suppressHydrationWarning>
        {children}
      </body>
    </html>
  );
}
