# Plano de Implementação — Atualização Visual G-2 (Maffeng)

Migrar o visual do `G-2` (Maffeng Gerenciador de Ordens de Serviço) do sistema "Ocean Breeze" para a estética Premium do `TM Hub`, mantendo a fidelidade total ao layout e fluxos atuais.

## Revisão do Usuário Requerida

> [!IMPORTANT]
> A estrutura de Dashboard (com Heatmap de atividade), Agenda com Checklist e o fluxo de Importação será preservada integralmente. A mudança focará em tipografia, paleta de cores, sombras e refinamento de componentes UI.

## Mudanças Propostas

### [Design System & Estética]

#### [MODIFICAR] [globals.css](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/G-2/MAFFENG-GERENCIADOR-DE-ORDENS-DE-SERVICO/styles/globals.css)
- Substituir a paleta `#f0f8ff` (Ocean Breeze) pelo fundo `#f0f4f3` do TM Hub.
- Atualizar a cor primária de `#22c55e` (Verde Padrão) para o `#00C896` (TM Emerald).
- Implementar as fontes `Syne` (títulos) e `DM Sans` (corpo).

### [Componentes Principais]

#### [MODIFICAR] [Dashboard.tsx](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/G-2/MAFFENG-GERENCIADOR-DE-ORDENS-DE-SERVICO/components/Dashboard.tsx)
- **Cards KPI**: Adicionar ícones com fundos em tons pastéis e bordas sutis.
- **Gráficos**: Ajustar as cores do Recharts para a paleta TM (Emerald, Blue, Amber, Red).
- **Heatmap**: Refinar a grade de atividade semanal para usar quadrados suaves com arredondamento padrão `radius-md`.

#### [MODIFICAR] [AgendaAndChecklist.tsx](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/G-2/MAFFENG-GERENCIADOR-DE-ORDENS-DE-SERVICO/components/AgendaAndChecklist.tsx)
- **Calendário**: Atualizar o seletor de mês e as células dos dias com o novo design de bordas e destaque de "Hoje".
- **Checklist**: Refinar os itens da lista com maior espaçamento e badges de prioridade mais elegantes.

## Plano de Verificação

### Verificação Manual (Preview)
- Validar se a transição entre as abas do Dashboard e Agenda está fluida no preview HTML.
- Garantir que o Heatmap de atividade reflete a intensidade corretamente através das cores.
- Confirmar se o design do "Checklist" mantém a legibilidade das tarefas vinculadas a O.S.
