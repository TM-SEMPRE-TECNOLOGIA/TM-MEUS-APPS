# AUDITORIA COMPLETA — DUPLICIDADE DE PASTAS E CONFIGURAÇÕES
**Data:** 2026-04-23  
**Repositório:** TM-MEUS-APPS  
**Status:** COMPLETO — Aguardando execução das ações

---

## Resumo Executivo

O repositório apresenta **11 duplicidades críticas** em múltiplos níveis hierárquicos. Pastas de configuração (`.agent/`, `.agents/`, `.jarvis/`, `.context/`, `skills/`) aparecem em 3 a 4 níveis diferentes com conteúdo parcialmente sobreposto. Potencial de limpeza estimado: **~550MB**.

---

## 1. `.agent/` vs `.claude/` — RAIZ

🔴 **DESTRUÍVEL**

- `.agent/skills/` contém `th-designer` e `ui-ux-pro-max` em versões **obsoletas**
- `.claude/skills/` tem versões superiores (ex: ui-ux-pro-max expandido)
- `.agent/` é resquício de migração anterior

**Ação:** Deletar recursivamente `/TM-MEUS-APPS/.agent/`

---

## 2. `.agents/` — RAIZ

🟡 **CONSOLIDÁVEL**

- Contém `logs/diario_de_dev.md` (único) + `skills/find-skills/` (linkado por symlink de `.claude/`)
- O symlink em `.claude/skills/find-skills → .agents/skills/find-skills` é funcional mas pode ser simplificado

**Ação:** Mover `diario_de_dev.md` para `.claude/logs/`, copiar `find-skills` localmente e remover symlink

---

## 3. `.jarvis/` — MÚLTIPLOS NÍVEIS

🔴 **DESTRUÍVEL** (em 02 e 03) | 🟡 **CONSOLIDÁVEL** (em 01_Golden)

Ocorrências:
- `01_Golden_Apps_meu_uso/.jarvis/` — versão mais completa (th-designer, squads)
- `02_Golden_Apps_Deploy/.jarvis/` — cópia desatualizada de 01
- `03_Arquivo_Morto_Legado/.jarvis/` — idêntica a 02 (arquivo morto)
- `.claude/worktrees/stoic-merkle/.jarvis/` — isolamento de worktree (esperado)

O `.jarvis/` de `01_Golden_Apps_meu_uso` é da **era anterior** ao sistema `.claude/skills/`. Contém:
- `global_rules.md` — regras antigas (superado pelo CLAUDE.md atual)
- `turbo_dev_skills.md` — skills antigas (migradas para `.claude/skills/`)
- `.agents/workflows/` — turbo-* antigos
- `th-design-squad.md` — único arquivo com possível valor residual
- `claude.bat` / `claude.ps1` — scripts de boot obsoletos
- `.ag_pixel_state` — estado legado do Pixel Agents

**Ação:** Revisar `th-design-squad.md`, depois deletar `.jarvis/` de todos os níveis

---

## 4. `.context/` — MÚLTIPLOS APPS

🟢 **NECESSÁRIO**

| Pasta | Arquivos |
|-------|----------|
| `AutoRelatorioV1_Dev/.context/` | `frontend_report.md`, `planning.md`, vídeo |
| `AutoRelatorio_V2/.context/` | `planning.md` |
| `AutoRelatorio_SaaS/.context/` | **vazia** |

**Ação:** Manter V1 e V2. Remover pasta vazia em SaaS se não necessária.

---

## 5. `skills/` — OPENSQUAD (MÚLTIPLOS NÍVEIS)

🟢 **NECESSÁRIO** (propósitos distintos)

| Caminho | Conteúdo |
|---------|----------|
| `.claude/skills/` | th-designer, ui-ux-pro-max, find-skills |
| `opensquad/.claude/skills/` | Skills core do framework |
| `opensquad/skills/` | Integrações externas (apify, canva, instagram...) |
| `opensquad/templates/ide-templates/*/skills/` | Templates multi-IDE |

**Ação:** Manter estrutura. Documentar separação core vs integrations.

---

## 6. `squad-brainstorming/` e `squad-docfactory/` — 01_Golden_Apps

🟡 **CONSOLIDÁVEL** (mas com propósitos distintos)

| Squad | Status | Conteúdo |
|-------|--------|----------|
| `squad-brainstorming/` | Em progresso | `diario_de_dev.md`, output de brainstorming |
| `squad-docfactory/` (raiz) | Completo | Dashboard React, src/, package.json, outputs |
| `squad-docfactory/` (worktree) | Isolado | Cópia de branch (comportamento esperado) |

**Ação:** Manter separados. O worktree é necessário para isolamento git.

---

## 7. `CLAUDE.md` — MÚLTIPLOS LOCAIS

🔴 **DESTRUÍVEL** (em arquivo morto)

| Arquivo | Status |
|---------|--------|
| `antigravity-awesome-skills/CLAUDE.md` | Manter (upstream) |
| `opensquad/CLAUDE.md` | Manter (necessário) |
| `03_Arquivo_Morto_Legado/.NEXT APPS/TURBO DEV/CLAUDE.md` | Deletar |
| `03_Arquivo_Morto_Legado/.NEXT APPS 2/TURBO DEV/CLAUDE.md` | Deletar |

---

## 8. `memory/` — SEM DUPLICIDADE

✅ Nenhuma pasta `memory/` duplicada encontrada fora do contexto esperado.

---

## CHECKLIST DE AÇÕES

### 🔴 Deletar Imediatamente
- [ ] `/TM-MEUS-APPS/.agent/` inteira (~50MB)
- [ ] `01_Golden_Apps_meu_uso/.jarvis/` (após revisar `th-design-squad.md`)
- [ ] `02_Golden_Apps_Deploy/.jarvis/`
- [ ] `03_Arquivo_Morto_Legado/.jarvis/`
- [ ] `CLAUDE.md` dentro de `03_Arquivo_Morto_Legado/`

### 🟡 Consolidar
- [ ] Mover `.agents/logs/diario_de_dev.md` → `.claude/logs/`
- [ ] Remover symlink `find-skills` e copiar localmente
- [ ] Remover `AutoRelatorio_SaaS/.context/` (vazia)

### 🗄️ Arquivar Externamente
- [ ] `03_Arquivo_Morto_Legado/` (~500MB) — mover para HD externo

### 🟢 Manter
- [ ] `.claude/skills/` (raiz) — configuração ativa
- [ ] `squad-brainstorming/` + `squad-docfactory/` (raiz) — propósitos distintos
- [ ] `opensquad/templates/ide-templates/` — multi-IDE support
- [ ] `.context/` de V1 e V2 — contextos específicos por versão

---

## Estrutura Alvo Após Limpeza

```
TM-MEUS-APPS/
├── .claude/
│   ├── skills/          ← fonte única de verdade para skills
│   │   ├── th-designer/
│   │   ├── ui-ux-pro-max/
│   │   └── find-skills/
│   ├── logs/
│   └── settings.local.json
├── 01_Golden_Apps_meu_uso/
│   ├── .claude/worktrees/stoic-merkle/
│   ├── AutoRelatorioV1_Dev/.context/
│   ├── AutoRelatorio_V2/.context/
│   ├── squad-brainstorming/
│   └── squad-docfactory/
├── 02_Golden_Apps_Deploy/     ← sem .jarvis
├── .NEXT APPS/TURBO DEV/opensquad/
│   ├── .claude/skills/
│   ├── skills/
│   └── templates/ide-templates/
└── [BACKUP EXTERNO: 03_Arquivo_Morto_Legado/]
```
