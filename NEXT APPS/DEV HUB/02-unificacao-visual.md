# 🎨 Plano de Unificação Visual — TM Design System v2 (LIGHT)

> Objetivo: Todos os apps TM devem transparescer a identidade da empresa com tema **CLARO**.  
> Futuramente: seletor para alternar para tema escuro.  
> Referências:
> - **HUb-client.html** — Light, azul, elegant, Inter font
> - **TM Extrator** — Light com tokens `--TM-*`, já tem `.dark` toggle
> - **G-2** — Light shadcn, limpo, profissional

---

## Decisão de Design: Por quê LIGHT?

O Thiago aprovou 3 referências que são predominantemente claras:

| Referência | Background | Primary | Estilo |
|------------|-----------|---------|--------|
| HUb-client.html | `#f0f4ff` (azul claro) | `#4f6ef7` (azul royal) | Cards brancos, borders sutis |
| TM Extrator | `#f0f8ff` (alice blue) | `#22c55e` (verde) | Glassmorphism light, gradients suaves |
| G-2 | `#ffffff` (branco puro) | `#030213` (quase preto) | shadcn clean, minimalista |

---

## Paleta Unificada TM — Tema Claro (Principal)

A paleta combina o **azul elegante** do Hub com o **layout limpo** do TM Extrator:

```css
:root {
  /* ═══ TM DESIGN SYSTEM v2 — LIGHT ═══ */

  /* ── Background ── */
  --tm-bg:             #f0f4ff;    /* fundo geral — azulado suave (Hub) */
  --tm-bg-card:        #ffffff;    /* cards e painéis */
  --tm-bg-hover:       #f8faff;    /* hover em cards */
  --tm-bg-input:       #f8faff;    /* campos de input */
  --tm-bg-sidebar:     #ffffff;    /* sidebar */

  /* ── Brand TM ── */
  --tm-primary:        #4f6ef7;    /* azul royal TM — identidade principal */
  --tm-primary-hover:  #3b5ce0;    /* hover do primary */
  --tm-secondary:      #8b5cf6;    /* roxo — destaque secundário */
  --tm-accent:         #10b981;    /* verde — ações de sucesso */
  --tm-gradient:       linear-gradient(135deg, #4f6ef7, #8b5cf6);

  /* ── Status ── */
  --tm-success:        #10b981;
  --tm-danger:         #ef4444;
  --tm-warning:        #f59e0b;
  --tm-info:           #06b6d4;

  /* ── Texto ── */
  --tm-text:           #111827;    /* texto principal */
  --tm-text-muted:     #6b7280;    /* texto secundário */
  --tm-text-subtle:    #9ca3af;    /* texto sutil */

  /* ── Bordas ── */
  --tm-border:         #e4e9f5;    /* borda padrão */
  --tm-border-hover:   #c9d4ff;    /* borda ao hover */

  /* ── Sombras ── */
  --tm-shadow:         0 1px 3px rgba(79, 110, 247, 0.08), 
                       0 4px 16px rgba(79, 110, 247, 0.06);
  --tm-shadow-hover:   0 4px 12px rgba(79, 110, 247, 0.15), 
                       0 12px 32px rgba(79, 110, 247, 0.1);

  /* ── Tipografia ── */
  --tm-font:           'Inter', system-ui, sans-serif;

  /* ── Radius ── */
  --tm-radius-sm:      6px;
  --tm-radius-md:      8px;
  --tm-radius-lg:      14px;
  --tm-radius-xl:      16px;
}
```

## Tema Escuro (Futuro — Toggle)

```css
.dark {
  --tm-bg:             #0d1117;
  --tm-bg-card:        rgba(22, 27, 34, 0.75);
  --tm-bg-hover:       rgba(22, 27, 34, 0.9);
  --tm-bg-input:       rgba(0, 0, 0, 0.4);
  --tm-bg-sidebar:     #161b22;

  --tm-primary:        #58a6ff;
  --tm-primary-hover:  #79b8ff;
  --tm-secondary:      #8b5cf6;
  --tm-accent:         #3fb950;

  --tm-text:           #e6edf3;
  --tm-text-muted:     #7d8590;
  --tm-text-subtle:    #484f58;

  --tm-border:         #30363d;
  --tm-border-hover:   #484f58;

  --tm-shadow:         0 1px 3px rgba(0, 0, 0, 0.3);
  --tm-shadow-hover:   0 4px 12px rgba(0, 0, 0, 0.4);
}
```

---

## Componentes Compartilhados

### 1. Header TM
```
┌──────────────────────────────────────────────────────────┐
│ [Logo TM]  HUB TM  │  🔍 Buscar...  │  ● Online  [TN]  │
└──────────────────────────────────────────────────────────┘
```
- Background branco com `backdrop-filter: blur(10px)`
- Border bottom sutil `#e4e9f5`
- Logo com gradiente azul → roxo

### 2. Cards (Tool Cards)
- Background branco `#ffffff`
- Border `1.5px solid #e4e9f5`
- Border-radius `14px`
- Hover: `translateY(-3px)` + sombra azul
- Accent line no topo (3px, cor do app)

### 3. Sidebar
- Background branco
- Items com hover `#f0f4ff`
- Item ativo: background `#eef2ff`, texto `#4f6ef7`

### 4. Botões
- **Primary**: bg `#4f6ef7`, texto branco, radius `8px`
- **Ghost**: bg branco, border sutil, texto cinza
- **Danger**: bg `#ef4444`

### 5. Inputs
- Background `#f8faff`
- Border `1.5px solid #e4e9f5`
- Focus: border `#4f6ef7` + ring `rgba(79, 110, 247, 0.1)`

---

## O que muda em cada App

| App | Esforço | Ação |
|-----|---------|------|
| **TM Relatorio** | 🟡 Médio | Trocar tema dark inteiro por light. Manter estrutura. |
| **TM Comparador** | 🟡 Médio | Trocar tema dark por light. Layout já bom. |
| **TM Ordens** | 🟡 Médio | Trocar tema dark por light. CSS classes → tokens `--tm-*`. |
| **TM Pastas** | 🟢 Baixo | Já tem tokens separados! Trocar valores para light. |
| **Bot Chat** | 🔴 Alto | Aplicar design system inteiro (não tem nada). |
| **G-2** | 🟢 Baixo | Já é light! Padronizar nomes de tokens para `--tm-*`. |
| **TM Extrator** | 🟢 Baixo | Já é light com `--TM-*`! Maior inspiração. Padronizar. |
| **Legacy SP** | ⚪ N/A | Desktop Tkinter — apenas card/atalho no Hub. |

## Hierarquia de Cores por App

No Hub, cada app terá uma cor de destaque própria, mantendo a identidade:

| App | Cor de Destaque | Uso |
|-----|----------------|-----|
| TM Relatorio | `#4f6ef7` (azul) | accent line no card |
| TM Comparador | `#10b981` (verde) | accent line no card |
| TM Ordens | `#f59e0b` (âmbar) | accent line no card |
| TM Pastas | `#06b6d4` (ciano) | accent line no card |
| Bot Chat | `#8b5cf6` (roxo) | accent line no card |
| G-2 | `#f59e0b` (âmbar) | accent line no card |
| TM Extrator | `#22c55e` (verde) | accent line no card |
