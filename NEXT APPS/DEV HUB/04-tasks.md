# 📋 TM Hub — Master Task List

> Checklist de todas as tarefas. Atualizado conforme progresso.

## 📄 Documentação
- [/] `01-diagnostico-apps.md` — 9 apps avaliados
- [x] `02-unificacao-visual.md` — Design System Light
- [/] `03-implementacao-hub.md` — Plano do Hub (atualizado para migrações)
- [/] `04-tasks.md` — Este checklist
- [/] `changelog.html` — Registro visual do projeto

## 🎯 Decisões Aprovadas
- [x] Aplicar exato design de compilação preview-hub-light.html (Light theme)
- [x] MIGRAR TUDO PARA NEXT.JS! G-2, Extrator, e Studio Relatorio devem ser refatorados para Next.js 16.

## Fase 1 — Fundação do Hub
- [ ] Criar projeto Next.js
- [ ] Design System v2 (tokens + components a partir do preview HTML)
- [ ] Grid de ferramentas com cards dinâmicos
- [ ] Backend FastAPI (health check, apps.json)
- [ ] `run_hub.bat`

## Fase 2 — Admin
- [ ] Auth simples (admin/user)
- [ ] Dashboard de status
- [ ] Gerenciamento de apps (on/off visual)

## Fase 3 — Integração de Portas
- [ ] TM Relatorio → 3001/5001
- [ ] TM Ordens → 3002/5002
- [ ] TM Comparador → 3003/5003
- [ ] TM Pastas → 3004/5004
- [ ] Bot Chat → 3005/5005
- [ ] TM Relatorio SP → 3008/5008
- [ ] Atualizar todos os bat files

## Fase 4 — Unificação Visual (Apps Next.js Atuais)
- [ ] Design System Light em TM Comparador
- [ ] Design System Light em TM Ordens
- [ ] Design System Light em TM Relatorio
- [ ] Design System Light em TM Pastas
- [ ] Design System Light em TM Relatorio SP
- [ ] Reskin Bot Chat
- [ ] Header TM em cada app

## Fase 5 — Migrações (Vite -> Next.js)
- [ ] Refatorar TM Extrator para Next.js (Porta 3007)
- [ ] Refatorar G-2 para Next.js (Porta 3006)
- [ ] Refatorar TM Studio Relatório para Next.js (Porta 3009)
