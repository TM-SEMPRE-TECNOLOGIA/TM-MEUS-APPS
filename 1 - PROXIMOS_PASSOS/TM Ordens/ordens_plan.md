# Plano de Implementação — Atualização Visual TM Ordens

Modernizar o visual do `TM Ordens` (Gestor de Ordens de Serviço) para o padrão do `TM Hub`, preservando rigorosamente o layout do Dashboard e as funcionalidades de gestão.

## Revisão do Usuário Requerida

> [!IMPORTANT]
> A estrutura de Cards KPI, Gráficos Recharts e Feed de Atividade Recente será mantida exatamente como está no código atual, apenas com aplicação de estilos e tokens de design modernos.

## Mudanças Propostas

### [Componente Frontend - Next.js]

#### [MODIFICAR] [globals.css](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/TM%20Ordens/frontend/app/globals.css)
- Migrar do tema escuro para o tema claro com acentos em verde esmeralda.
- Aplicar tipografia `Syne` para títulos de KPIs e `DM Sans` para descrições.
- Suavizar sombras e bordas dos painéis de vidro (glassmorphism) para o novo padrão.

#### [MODIFICAR] [page.tsx](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/TM%20Ordens/frontend/app/page.tsx)
- **KPI Cards**: Atualizar as cores de fundo secundárias para tons pastéis suaves que acompanham os ícones coloridos.
- **Gráfico de Status**: Ajustar as cores do Recharts para a nova paleta do Hub (Primário, Sucesso, Alerta, Perigo).
- **Recent Activity**: Refinar o feed de atividades com maior espaçamento e tipografia clara.

## Plano de Verificação

### Verificação Manual
- Garantir que a renderização dos gráficos de barras mantém a interatividade do Tooltip.
- Validar se os emblemas (Badges) de situação da OS estão com as cores corretas e legíveis.
- Confirmar se o efeito de fade-in na carga da página permanece fluido.
