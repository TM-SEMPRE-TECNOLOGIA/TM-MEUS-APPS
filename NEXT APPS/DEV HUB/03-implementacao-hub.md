# 🏗️ Plano de Implementação — TM Hub (Next.js Completo)

> Hub central estilo iLovePDF para todos os apps TM.  
> Tema LIGHT como padrão, com toggle dark futuro.  
> **TODOS os apps serão unificados e migrados para Next.js.**

---

## Arquitetura

```
TM Hub (Next.js 16 + FastAPI)
  │
  ├── 👤 Visão Usuário ── Ferramentas (grid de apps)
  │   ├── Busca, filtro por categoria, favoritos
  │   └── Clicar → abre app em nova aba
  │
  ├── 🔐 Visão Admin ── Tudo + extras
  │   ├── Dashboard com status online/offline
  │   ├── Gerenciar apps (adicionar/editar)
  │   ├── Configurações
  │   └── Área de arquivos
  │
  └── ⚙ Backend FastAPI
      ├── Health check dos apps
      ├── Registro de apps (apps.json)
      ├── Auth simples (admin/user)
      └── Storage API
```

## Apps Registrados (9 total programados para Next.js)

| # | App | Categoria | FE Port | BE Port |
|---|-----|-----------|---------|---------|
| 1 | TM Relatorio | Documentos | 3001 | 5001 |
| 2 | TM Comparador | Análise | 3003 | 5003 |
| 3 | TM Ordens | Gestão | 3002 | 5002 |
| 4 | TM Pastas | Utilidades | 3004 | 5004 |
| 5 | Bot Chat | IA | 3005 | 5005 |
| 6 | G-2 (Migrar Next.js) | Gestão | 3006 | 5006 |
| 7 | TM Extrator (Migrar Next.js) | Documentos | 3007 | 5007 |
| 8 | TM Relatorio SP | Documentos | 3008 | 5008 |
| 9 | TM Studio Relatorio (Migrar Next.js)| UI | 3009 | 5009 |

## Fases Atualizadas (Migração Total Next.js)

### Fase 1 — Fundação do Hub
- Criar projeto Next.js do Hub com Design System Light
- Grid de apps funcional com cards (abrir em nova aba)
- Backend com health check e registro `apps.json`

### Fase 2 — Admin + Auth
- Login simples, toggle admin/user
- Dashboard de status dos apps

### Fase 3 — Integração e Portas
- Reconfigurar portas de todos os apps que já estão em Next.js
- Atualizar bat files e `run_all.bat` master

### Fase 4 — Unificação Visual dos Apps em Next.js
- Aplicar Design System v2 Light em cada app (Relatório, Comparador, Ordens, Pastas, SP)
- Header TM compartilhado com botão "← Hub"
- Reskin Bot Chat

### Fase 5 — Migrações Vite para Next.js (Massa Crítica)
- Migrar G-2 (Vite -> Next.js) aplicando referências shadcn + Light Layout
- Migrar TM Extrator (Vite -> Next.js) aproveitando os tokens CSS `--TM-*`
- Migrar TM Studio Relatorio (Vite -> Next.js)
