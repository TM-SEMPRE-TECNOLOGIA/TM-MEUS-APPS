# 🔍 Diagnóstico Individual dos Apps — TM Hub

> Documento gerado em 2026-03-04 | Reanálise completa com TODOS os apps  
> Referências visuais: **HUb-client.html** (light) · **TM Extrator** (light + dark toggle) · **G-2** (light shadcn)

---

## 1. TM Relatorio — Gerador de Relatórios DOCX

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/TM Relatorio` |
| **Framework** | Next.js 16 + Tailwind 4 |
| **Backend** | FastAPI (`server.py`) |
| **Portas** | FE: `3000` · BE: `5000` |
| **Tema** | Cyber-Dark (escuro: `#010409`, azul `#58a6ff`) |
| **Ação** | Migrar CSS para novo design system unificado (Light). Trocar fundo escuro. |

---

## 2. TM Comparador — Comparador Excel × DOCX

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/TM Comparador` |
| **Framework** | Next.js 16 + Tailwind 4 |
| **Backend** | FastAPI (`server.py`) |
| **Portas** | FE: `3000` · BE: `5000` |
| **Tema** | Cyber-Dark (escuro: `#0d1117`, ciano `#00d4ff`) |
| **Ação** | Migrar CSS, realocar portas |

---

## 3. TM Ordens — Gerenciador de Ordens de Serviço

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/TM Ordens` |
| **Framework** | Next.js 16 + Tailwind 4 |
| **Backend** | FastAPI (`server.py`) |
| **Portas** | FE: `3002` · BE: `5002` ✅ |
| **Tema** | Cyber-Dark (escuro: `#0d1117`, ciano `#00d4ff`) |
| **Ação** | Migrar CSS para design system light |

---

## 4. TM Pastas — Gerador de Pastas

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/TM Pastas` |
| **Framework** | Next.js 16 + Tailwind 4 |
| **Backend** | FastAPI (`backend/api.py`) |
| **Portas** | FE: `3000` · BE: `5000` |
| **Tema** | Cyber-Dark (`#0a0a0f`) — tem design system separado (tokens.css) |
| **Ação** | Atualizar tokens para light, realocar portas |

---

## 5. Bot Chat — Chat Bot com IA

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/Bot-chat-next.js` |
| **Framework** | Next.js 16 + Tailwind 4 |
| **Backend** | Python (`main.py`) + OpenAI |
| **Portas** | FE: `3000` |
| **Tema** | ❌ Sem tema — CSS default Next.js |
| **Ação** | Aplicar design system completo, criar bat |

---

## 6. G-2 — Gerenciador de O.S. V2 (MAFFENG)

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/G-2/MAFFENG-GERENCIADOR-DE-ORDENS-DE-SERVICO` |
| **Framework** | ⚠️ **Vite** + React 18 (migrando para Next.js) |
| **Backend** | Express + PostgreSQL + Drizzle ORM |
| **Tema** | ✅ **Light shadcn** (`#ffffff` bg, clean) — com `.dark` variant |
| **Ação** | **MIGRAR PARA NEXT.JS**. G-2 já usa light theme similar ao desejado. |

---

## 7. TM Extrator — Extrator de DOCX

| Item | Valor |
|------|-------|
| **Pasta** | `TM Extrator` (fora do NEXT APPS) |
| **Framework** | ⚠️ **Vite** + React 19 (migrando para Next.js) |
| **Tema** | ✅ **MELHOR referência LIGHT** — vars `--TM-*`, com `.dark` toggle |
| **Ação** | **MIGRAR PARA NEXT.JS**. Base inspiração para o design system unificado. |

---

## 8. TM Relatorio SP — Gerador Relatório SP

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/TM Relatorio SP` |
| **Framework** | Next.js 16 + Tailwind 4 |
| **Backend** | FastAPI (`server.py`) |
| **Tema** | Cyber-Dark |
| **Ação** | Substitui o antigo Legacy Tkinter. Precisa ir para o tema Light e nova porta. |

---

## 9. TM Studio Relatorio

| Item | Valor |
|------|-------|
| **Pasta** | `NEXT APPS/TM STUDIO RELATORIO` |
| **Framework** | ⚠️ **Vite** + React 19 (migrando para Next.js) |
| **Ação** | **MIGRAR PARA NEXT.JS**. Incorporar ao Hub. |

---

## 📊 Resumo Comparativo

| App | Framework Atual | Destino Final | Tema Atual |
|-----|-----------|---------|------------|
| TM Relatorio | Next.js 16 | Next.js | 🌑 Dark |
| TM Relatorio SP | Next.js 16| Next.js | 🌑 Dark |
| TM Comparador | Next.js 16 | Next.js | 🌑 Dark |
| TM Ordens | Next.js 16 | Next.js | 🌑 Dark |
| TM Pastas | Next.js 16 | Next.js | 🌑 Dark |
| Bot Chat | Next.js 16 | Next.js | ❌ Nenhum |
| G-2 | Vite | **Next.js** | ☀️ Light |
| TM Extrator | Vite | **Next.js** | ☀️ Light+Dark |
| TM Studio Relat. | Vite | **Next.js** | Varia |

### Alocação de Portas Proposta

| App | Frontend | Backend |
|-----|----------|---------|
| **TM Hub** | `3000` | `5000` |
| TM Relatorio | `3001` | `5001` |
| TM Ordens | `3002` | `5002` |
| TM Comparador | `3003` | `5003` |
| TM Pastas | `3004` | `5004` |
| Bot Chat | `3005` | `5005` |
| G-2 | `3006` | `5006` |
| TM Extrator | `3007` | `5007` |
| TM Relatorio SP | `3008` | `5008` |
| TM Studio Relat. | `3009` | `5009` |
