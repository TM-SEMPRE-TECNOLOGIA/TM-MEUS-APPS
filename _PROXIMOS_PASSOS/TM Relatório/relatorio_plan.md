# 🎨 Plano de Refatoração: TM Relatório (Design System Light)

## 🎯 Objetivo
Trazer o **TM Relatório** do legado "Cyber-Dark" para o novo design padronizado da Fáblica de SaaS TM (Design System Light), seguindo as diretrizes firmadas no `MASTER_PLAN_360.md`. A referência visual principal será o novo **Hub / TM Extrator**.

## 🏗️ Estrutura Atual vs Nova
- **Atual**: Tema escuro (preto/ciano), variáveis CSS genéricas, cards opacos.
- **Novo**: Tema claro (branco/azul royal), tokens CSS precisos (`--tm-*`), backgrounds em `f0f4ff`, cards brancos com leve sombra (`tm-shadow`), botões azuis e feedback verde (`#10b981`).

## 🛠️ Modificações Necessárias no Next.js (`TM Relatório`)

### 1. Refatoração do `globals.css`
- Substituir completamente o `:root` dark pelo conjunto de tokens `--tm-*` Light Theme definidos na documentação do HUB.
- Garantir a presença de classes utilitárias base como:
  - `.tm-bg-app` (background geral da tela inteira)
  - `.tm-card` (cartões brancos, rounded-xl, shadow e borda hover)
  - `.tm-input-field` e `.tm-btn-primary`

### 2. Atualização dos Componentes React (`page.tsx`)
- Remover fundos forçados escuros em hardcode como `bg-gray-900`.
- Aplicar o layout do `TM Header`:
  - `header` com fundo glassmorphism claro.
  - Logotipo em Gradiente TM (Azul `4f6ef7` para Roxo `8b5cf6`).
- As caixas brancas dos passos (Selecione a Pasta, Tipo de Relatório) passarão a utilizar a classe unificada `.tm-card`.

### 3. Paleta de Cores e Portas
- **Cor Primária Accent**: `--tm-primary: #4f6ef7`
- **Portas Atribuídas**: UI em `:3001` / API em `:5001`. As configurações `.env` e chamadas `fetch` dentro do FE precisarão ser mapeadas para essa porta correta.

## ✅ Critérios de Aceite
- O app inicia sem erros e responde às integrações Python na porta `:5001`.
- A interface visual é 100% clara (Light), exibindo botões padronizados azuis e verdes.
- O componente de Timeline de Geração do relatório encaixa harmonicamente nas cores suaves sem comprometer a leitura.

*(O protótipo visual esperado foi gerado em `relatorio_preview.html` junto deste diretório)*
