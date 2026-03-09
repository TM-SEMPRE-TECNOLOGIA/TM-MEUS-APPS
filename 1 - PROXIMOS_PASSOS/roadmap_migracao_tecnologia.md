# ⚛️ Roadmap de Migração Tecnológica (Next.js)

O objetivo estratégico para o "TM Hub" é o modelo SaaS Factory. Para prover escalabilidade, SEO, performance de renderização no servidor (SSR) e facilidades analíticas, **todos os aplicativos TM devem ser migrados para o Next.js (versão 13+ com App Router recomendado ou superior)**. 

Atualmente temos uma infraestrutura híbrida. Abaixo o plano estratégico e a ordem recomendada de migração de tecnologia.

## 📊 Status de Tecnologia Atual

| Aplicativo | Framework Atual | Status de Migração | Prioridade |
|------------|-----------------|--------------------|------------|
| **TM Hub (Core)** | `N/A (Apenas HTML)` | 🔴 Precisa ser criado em Next.js | Máxima |
| **TM Extrator 2.0**| `Vite (React JS)` | 🔴 Necessita migração | Alta |
| **G-2 (Maffeng)** | `Vite (React JS)` | 🔴 Necessita migração | Média |
| **TM Relatório SP**| `Next.js` | ✅ Já está em Next.js | Concluído (Refatorar apenas Design) |
| **TM Pastas** | `Next.js` | ✅ Já está em Next.js | Concluído (Refatorar apenas Design) |
| **TM Comparador** | `Next.js` | ✅ Já está em Next.js | Concluído (Refatorar apenas Design) |
| **TM Ordens** | `Next.js` | ✅ Já está em Next.js | Concluído (Refatorar apenas Design) |

## 🚀 Rota de Migração e Estratégia de Execução

As migrações tecnológicas ocorrerão paralelamente ou imediatamente antes/durante as atualizações de redesign do **Ocean Breeze v2.0**.

### 1. Inicialização do DEV HUB (Core)
*   **Ação:** Criar do zero a estrutura Next.js para o portal (`0 - NEXT APPS/DEV HUB`).
*   **Por quê:** Servirá de molde. Configurar o Tailwind, roteamento principal, e infraestrutura "SaaS" para ditar as regras dos demais apps se/quando eles passarem a viver no mesmo repositório (Monorepo) ou mesma hospedagem.

### 2. Migração `TM Extrator 2.0` (Vite ➔ Next.js)
*   **Ação:** Construir uma nova base Next.js (ex: `tm-extrator-next`) em vez do atual APP em Vite.
*   **Estratégia:** 
    1. Criar a estrutura Next.js "App Router".
    2. Importar o `App.jsx` atual e extrair lógicas PURE REACT em Server/Client components.
    3. Migrar toda a parte visual baseando na Sidebar de Processo (Ocean Breeze).
*   **Vantagens:** O Extrator Rápido vai aproveitar melhor cache do lado do cliente do Next e ter perfis de desempenho mais estáveis com arquivos massivos se usarmos API Routes para operações off-thread do documento (se for via node) em vez de on-browser.

### 3. Migração `G-2 (Maffeng)` (Vite ➔ Next.js)
*   **Ação:** Durante o seu Update de Design Visual, reconstruir o G-2 diretamente dentro de um ambiente Next.js.
*   **Estratégia:** Como já existe um plano de redesign completo na gaveta `_PROXIMOS_PASSOS/G-2`, a execução deste plano deverá começar iniciando um `create-next-app` primeiro, em vez de aplicar código na base Vite atual.

## 🛠 Padrão de Projeto sugerido para todos Next.js (TM Apps)
- Framework: Next.js (App Router `app/`)
- Estilização: TailwindCSS
- Ícones: Lucide React (ou nativos SVG exportados)
- State Management: React Context / Zustand (onde complexidade ditar)
- Deployment: Preparação `out/` estática ou Vercel dependendo do uso de Node.js via SSR/API.
