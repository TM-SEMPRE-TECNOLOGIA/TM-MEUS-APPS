# SKILLS MAP — TM-MEUS-APPS

Mapa completo de todas as skills e repositórios de apoio do ecossistema TURBO DEV.

---

## Skill Raiz

### `Skill_geral_prompt.md`

**Descrição:** Gerador de Prompt Técnico Estruturado. Transforma explicações livres em prompts organizados e precisos para ferramentas de IA.

**Como usar:** Descreva livremente o que precisa e a skill estrutura o pedido nas seções: Contexto, Problema, Issues Identificados, Objetivos, Regras Técnicas, Instruções e Questões de Alinhamento.

**Ideal para:** Correção de bugs, criação de features, refatoração, melhorias de arquitetura, documentação, criação de tarefas de desenvolvimento.

---

## Skills TURBO DEV

Ativadas via comandos `/turbo-X` a partir dos workflows em `.agents/workflows/`.

---

### `/turbo-ui`
**Arquivo:** `.agents/workflows/turbo-ui.md`
**Repositório de Apoio:** `ui-ux-pro-max-skill`
**GitHub:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill ⭐ 64.8k

**Descrição:** Ativa o motor de Design System **Ocean Breeze Premium**. Aplica paleta visual Esmeralda/Ciano com glassmorphism, dark mode nativo, micro-animações e componentes Framer Motion.

**Como usar:**
1. Ative com `/turbo-ui` antes de qualquer tarefa de UI
2. Use o script `search.py` para buscar inspiração de tokens (ex: `glassmorphism dark emerald`)
3. Aplique rigorosamente a paleta `#34d399` (Esmeralda) / `#06b6d4` (Ciano)
4. Siga os templates Framer Motion em `src/templates/` do repositório
5. Tipografia: Inter/Outfit para interface, nunca misture fontes arbitrárias

---

### `/turbo-prevc`
**Arquivo:** `.agents/workflows/turbo-prevc.md`
**Repositório de Apoio:** TURBO DEV root (`@ai-coders/context`)
**GitHub:** *(metodologia interna — sem repo externo)*

**Descrição:** Ativa a metodologia **PREVC da AI Coders Academy** para gestão estruturada de contexto. Garante que cada fase de desenvolvimento seja documentada e rastreável.

**Fases:** Planning → Review → Execution → Validation → Confirmation

**Como usar:**
1. Cada fase deve ser documentada em arquivos separados em `.context/`
2. Novos projetos seguem o scaffold: `app/`, `dev/`, `legacy/`, `documents/`, `scripts/`
3. Toda tarefa concluída gera sumário técnico no `commit.html` local e no `diario_de_dev.md`

---

### `/turbo-skills`
**Arquivo:** `.agents/workflows/turbo-skills.md`
**Repositório de Apoio:** `antigravity-awesome-skills`
**GitHub:** https://github.com/sickn33/antigravity-awesome-skills ⭐ 32.9k

**Descrição:** Ativa o catálogo de **1.400+ Prompts de Elite e Especialistas**. Permite buscar e carregar skills especializadas para temas complexos (Next.js, segurança, DevOps, IA/ML, etc.).

**Como usar:**
1. Ative com `/turbo-skills` quando a tarefa exigir expertise específica
2. Consulte `CATALOG.md` na raiz do repositório para encontrar o `@specialist` adequado
3. Carregue o arquivo de skill em `skills/` antes de responder
4. Mescle a inteligência do prompt de elite com o contexto atual do projeto

---

### `/turbo-gsd`
**Arquivo:** `.agents/workflows/turbo-gsd.md`
**Repositório de Apoio:** `get-shit-done`
**GitHub:** https://github.com/gsd-build/get-shit-done ⭐ 52.8k

**Descrição:** Ativa o motor de **Context Engineering ultra-eficiente** (GSD). Previne a degradação de contexto via planejamento XML estruturado e execução atômica — ideal para sessões longas.

**Como usar:**
1. Em projetos novos, inicialize com: `npx get-shit-done-cc@latest init`
2. Carregue os prompts de sistema em `templates/phase-prompt.md`
3. Gere planos XML com tags `<task>` e `<verification>` para cada tarefa
4. Nunca execute mais de 3 tarefas sem validar o status no `ROADMAP.md`

---

### `/turbo-crew`
**Arquivo:** `.agents/workflows/turbo-crew.md`
**Repositório de Apoio:** `crewAI`
**GitHub:** https://github.com/crewAIInc/crewAI ⭐ 48.8k

**Descrição:** Ativa a força-tarefa de **Agentes de Auditoria e QA Check** via CrewAI. Implementa revisão cruzada onde código só avança com aprovação do agente Auditor, usando fluxos event-driven.

**Como usar:**
1. Carregue as configurações de `agents.yaml` e `tasks.yaml` do repositório para definir personas
2. Siga o padrão de Flows (event-driven) para aprovação em cadeia
3. Para alterações críticas, simule auditoria cruzada: "Auditor AI revisando o código de Coder AI..."
4. Só marque a tarefa como concluída após aprovação do agente Auditor

---

### `/turbo-n8n`
**Arquivo:** `.agents/workflows/turbo-n8n.md`
**Repositório de Apoio:** `n8n-mcp`
**GitHub:** https://github.com/PageLines/n8n-mcp *(referência mais próxima ao `npx n8n-mcp`)*

**Descrição:** Ativa a orquestração de robôs e automações via **MCP do N8N**. Oferece acesso a 1.200+ nodes de integração com suporte a Webhooks, REST endpoints e schemas JSON.

**Como usar:**
1. Inicie o servidor com: `npx n8n-mcp`
2. Para integrações específicas (ex: Telegram), use a ferramenta de busca de nodes para obter a spec exata
3. Nunca edite workflows em produção — sempre gere o JSON em `dev/n8n/` para revisão
4. Siga os schemas JSON em `src/types/` do repositório para payloads

---

### `/turbo-pixel`
**Arquivo:** `.agents/workflows/turbo-pixel.md`
**Repositório de Apoio:** `pixel-agents`
**GitHub:** https://github.com/pablodelucca/pixel-agents ⭐ 6.5k

**Descrição:** Ativa a **interface visual Pixel Agents** onde agentes de IA são representados como personagens em um escritório pixel art. Integra transcritos JSONL para monitoramento visual em tempo real.

**Como usar:**
1. Abra o painel "Pixel Agents" no VS Code para visualizar os agentes
2. Descreva suas ações com estados claros: "lendo arquivo X", "escrevendo função Y", "executando teste Z"
3. Use a estética de "agentes como personagens" para comunicar progresso ao usuário
4. O transcrito JSONL é monitorado automaticamente pelo painel

---

### `/turbo-anthropic`
**Arquivo:** `.agents/workflows/turbo-anthropic.md`
**Repositório de Apoio:** `skills` (diretório local)
**GitHub:** *(skills oficiais Anthropic — distribuídas via Claude Code)*

**Descrição:** Ativa as ferramentas e skills **oficiais da Anthropic (The Standard)**. Oferece capacidades de manipulação de documentos e geração de relatórios profissionais em DOCX/PDF.

**Como usar:**
1. Liste as ferramentas disponíveis no diretório `skills/`
2. Use as skills de `Document Manipulation` para relatórios DOCX/PDF
3. Siga as guidelines de marca e tom de voz em `brand/`

---

### `/turbo-checkpoint`
**Arquivo:** `.agents/workflows/turbo-checkpoint.md`
**Repositório de Apoio:** *(protocolo interno — sem repo externo)*

**Descrição:** Ativa o **Protocolo Oficial de Checkpoint e Encerramento de Sessão**. Sincroniza o diário de desenvolvimento, logs HTML e Git de forma estruturada ao final de cada sessão.

**Como usar:**
1. Atualize `diario_de_dev.md` com Resumo Executivo (o que foi feito, decisões, o que falta)
2. Analise e proponha atualizações nos logs `commit_geral.html` e `commit.html` — aguarde aprovação do usuário
3. Revise as mudanças e crie mensagem de commit em Conventional Commits (`feat:`, `fix:`, `refactor:`)
4. Solicite permissão expressa antes de executar `git commit` e `git push`

---

### `/turbo-mono`
**Arquivo:** `.agents/workflows/turbo-mono.md`
**Repositório de Apoio:** `turborepo`
**GitHub:** https://github.com/vercel/turborepo ⭐ 28k+

**Descrição:** Ativa a orquestração de monorepo via **Turborepo (Vercel)**. Utiliza sistema de build baseado em Rust para cache distribuído e pipelines paralelos em múltiplos aplicativos.

**Como usar:**
1. Verifique sempre o `turbo.json` na raiz do monorepo para configurar tarefas
2. Use Turborepo para otimizar builds paralelos entre os apps do workspace
3. Aproveite o cache distribuído para evitar re-execução de tarefas já realizadas

---

## Resumo dos Repositórios de Apoio

| Skill | Repositório | GitHub | Stars |
|---|---|---|---|
| `/turbo-ui` | `ui-ux-pro-max-skill` | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | ⭐ 64.8k |
| `/turbo-skills` | `antigravity-awesome-skills` | https://github.com/sickn33/antigravity-awesome-skills | ⭐ 32.9k |
| `/turbo-gsd` | `get-shit-done` | https://github.com/gsd-build/get-shit-done | ⭐ 52.8k |
| `/turbo-crew` | `crewAI` | https://github.com/crewAIInc/crewAI | ⭐ 48.8k |
| `/turbo-pixel` | `pixel-agents` | https://github.com/pablodelucca/pixel-agents | ⭐ 6.5k |
| `/turbo-n8n` | `n8n-mcp` | https://github.com/PageLines/n8n-mcp | *(referência)* |
| `/turbo-mono` | `turborepo` | https://github.com/vercel/turborepo | ⭐ 28k+ |
| `/turbo-prevc` | *(interno)* | — | — |
| `/turbo-anthropic` | *(skills oficiais)* | — | — |
| `/turbo-checkpoint` | *(protocolo)* | — | — |

---

## Status dos Repositórios no Git

> **Atenção:** O diretório `.NEXT APPS/TURBO DEV/` está **vazio** no repositório Git.
> Todos os repositórios de apoio são referenciados nos workflows mas não estão presentes localmente neste ambiente — os caminhos usados nos arquivos de workflow apontam para a máquina Windows do desenvolvedor (`C:\Users\thiag\...`).

Para adicionar os repositórios ao ambiente, clone-os em `.NEXT APPS/TURBO DEV/`:

```bash
# Antigravity Awesome Skills
git clone https://github.com/sickn33/antigravity-awesome-skills ".NEXT APPS/TURBO DEV/antigravity-awesome-skills"

# UI/UX Pro Max Skill
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill ".NEXT APPS/TURBO DEV/ui-ux-pro-max-skill"

# Get-Shit-Done
git clone https://github.com/gsd-build/get-shit-done ".NEXT APPS/TURBO DEV/get-shit-done"

# CrewAI
git clone https://github.com/crewAIInc/crewAI ".NEXT APPS/TURBO DEV/crewAI"

# Pixel Agents
git clone https://github.com/pablodelucca/pixel-agents ".NEXT APPS/TURBO DEV/pixel-agents"
```
