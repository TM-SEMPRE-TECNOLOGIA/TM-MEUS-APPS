# 📑 Planning: Redesign Minimalista Industrial (AutoRelatorioV1)

**Fase:** Planejamento (P) - Metodologia PREVC
**Objetivo:** Migrar o frontend atual de "Ocean Breeze" para o estilo "Minimalista Industrial" (T1), mantendo a integridade funcional e elevando o nível estético.

---

## 👥 Orquestração de Agentes (CrewAI)

Configuramos uma equipe de especialistas para este projeto:

| Agente | Role | Goal |
| :--- | :--- | :--- |
| **@ui-lead** | Senior UI/UX Designer | Garantir a fidelidade ao estilo "Blueprint/Industrial" e a harmonia visual. |
| **@fe-architect** | Frontend Specialist | Traduzir o design em tokens CSS e componentes React/Next.js performantes. |
| **@prevc-auditor** | Quality & Process Lead | Assegurar o cumprimento da metodologia PREVC e a qualidade final do código. |

---

## 🔍 Análise do Estado Atual (Mapeamento)

### 🧩 Frontend Atual (Base)
- **Framework:** Next.js 15+ (App Router).
- **Estilização:** Tailwind CSS 4.0.
- **Paleta Atual:** Teal (#0d9488) e Slate.
- **Componentes Chave:** `SidebarWizard`, `PreviewGrid`, `ConsoleWatcher`.
- **Status:** Estabilizado e funcional (Checkpoint v28).

### 📐 Novo Design (Referência: `style-comparator-hub.html`)
- **Vibe:** Minimalista Industrial / Blueprint.
- **Cores:**
  - `bg-primary`: `#f0f4fa` (Gelo/Azul muito claro)
  - `brand-primary`: `#003694` (Azul Marinho Profundo)
  - `brand-accent`: `#8a5100` (Laranja/Ouro Industrial)
- **Tipografia:** 
  - `UI`: **Manrope** (Sério e moderno)
  - `Data`: **Space Grotesk** (Geométrico e técnico)
- **Formas:** Raio de borda de `8px` (Sóbrio).

---

## 🛠️ Roadmap de Implementação (Etapas)

### Etapa 1: Fundação de Design (@ui-lead + @fe-architect)
- [ ] **Definição de Tokens:** Criar o novo sistema de variáveis no `globals.css`.
- [ ] **Configuração de Fontes:** Integrar `Manrope` e `Space Grotesk` via font-face/Next Font.
- [ ] **Surface-on-Surface:** Definir os níveis de profundidade (L0: fundo, L1: sidebar, L2: cards).

### Etapa 2: Reestruturação do Core Layout (@fe-architect)
- [ ] **SidebarWizard:** Refatorar para o visual branco/clean do protótipo T1.
- [ ] **Header:** Atualizar logotipo e navegação para o estilo "Industrial Ledger".
- [ ] **ConsoleWatcher:** Implementar a barra de console com tipografia mono e cores técnicas.

### Etapa 3: Refinamento de Componentes (@ui-lead + @fe-architect)
- [ ] **PreviewGrid:** Ajustar os cards de fotos para o novo grid sem bordas pesadas.
- [ ] **Botões:** Implementar botões com gradientes sutis e micro-animações.

### Etapa 4: Auditoria e Validação (@prevc-auditor)
- [ ] Teste de contraste e acessibilidade.
- [ ] Validação do fluxo de usuário (Área > Ambiente > Scan).
- [ ] Geração do arquivo `review.md`.

---

## ⚠️ Riscos Identificados
- **Conflito de Versões:** Garantir que o Tailwind 4 não sofra regressões visuais durante a troca de temas.
- **Performance:** Manter a fluidez das animações de entrada de itens no grid.

---

## 🔍 Auditoria Técnica do Frontend Atual

Após análise ativa e navegação local, identificamos os seguintes pontos críticos que serão resolvidos durante esta migração:

### 🔴 Falhas Críticas
- **Charset/Encoding Mojibake:** Erros de renderização em toda a UI (`AnÃ¡lise`, `FunÃ§Ã£o`). **AÇÃO:** Sanatizar todos os arquivos `.tsx` para UTF-8.
- **Wizard Sem Validação:** O usuário pode navegar entre as etapas sem completar as anteriores. **AÇÃO:** Travar etapas futuras e adicionar feedback visual de "Locked".

### 🧩 Mapeamento de Integração (O que NÃO vai mudar)
- **RESTRIÇÃO ABSOLUTA E RESPONSABILIDADE INTOCADA:** A pedido do usuário, **toda e qualquer lógica de integração**, requisição de API (`page.tsx`), ou placeholders hardcoded com dados (como "C:\Users\Admin" ou "Desc 1, 2, 3") **NÃO SERÃO ALTERADOS**. Em time que está ganhando, não se mexe; a engenharia de backend e passagem de dados atual continua 100% igual. O escopo é estrita e exclusivamente visual.

### 📐 Débito Técnico
- **Tipagem `any`:** Vários componentes sem definição de tipo rigorosa.
- **Design Tokens Desatualizados:** `globals.css` ainda usa variáveis do antigo "Ocean Breeze".

---
*Relatório de Auditoria consolidado por @prevc-auditor*

---
> [!IMPORTANT]
> A execução deve ser estritamente sequencial. Não iniciaremos a Etapa 2 sem a aprovação da Etapa 1.

---
*Gerado via Turbo-Dev (Protocolo PREVC + CrewAI)*

