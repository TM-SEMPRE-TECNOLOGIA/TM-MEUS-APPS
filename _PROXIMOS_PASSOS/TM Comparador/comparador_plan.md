# Plano de Implementação — Atualização Visual TM Comparador

Migrar o `TM Comparador` do tema "Cyber-Dark" legado para o novo Design System (Light Theme) do `TM Hub`, unificando a experiência visual.

## Revisão do Usuário Requerida

> [!IMPORTANT]
> O aplicativo manterá seu layout de fluxo vertical (Seleção -> Comparação -> Resultados), mas adotará a estética de Sidebar para navegação entre ferramentas e controle de histórico, similar ao novo padrão do TM Extrator.

## Mudanças Propostas

### [Componente Frontend - Next.js]

#### [MODIFICAR] [globals.css](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/TM%20Comparador/frontend/app/globals.css)
- Substituir o tema escuro/neon por tons de branco, verde esmeralda e ciano.
- Implementar as fontes oficiais: `Syne` (Displays) e `DM Sans` (Interface).
- Refinar as tabelas de comparação para maior contraste e legibilidade de diferenças.

#### [MODIFICAR] [Componentes Individuais]
- **Dropzones de Comparação**: Criar componentes de upload lado a lado (Arquivo A vs Arquivo B) com feedback visual de "Match" ou "Divergência" imediato.
- **Painel de Resultados**: Implementar filtros rápidos para ver apenas "Diferenças", "Novos Itens" ou "Igualdade".
- **Header & Sidebar**: Integrar a Sidebar de navegação com o **Símbolo TM Oficial** e trilha de navegação (Breadcrumbs).

## Plano de Verificação

### Verificação Manual
- Validar a clareza das cores de destaque nas tabelas de comparação (ex: fundo vermelho suave para deletados, verde para novos).
- Testar o comportamento responsivo dos dois campos de upload em telas menores.
- Confirmar se o download do relatório de comparação (.xlsx) mantém a integridade funcional.
