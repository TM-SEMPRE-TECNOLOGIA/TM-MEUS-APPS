# Plano de Implementação — Atualização Visual TM Pastas (Alta Fidelidade)

Atualizar a estética do `TM Pastas` para o padrão moderno (Light Theme) do `TM Hub`, mantendo a estrutura funcional de "Wizard" e "Preview" intacta.

## Revisão do Usuário Requerida

> [!IMPORTANT]
> Esta atualização preserva rigorosamente o layout original de duas colunas, mas eleva o nível visual para o padrão "Cyber-Light" do Hub. 
> 
> **Foco da Geração**:
> - Reconstrução do Accordion do Wizard com estados ativo/inativo refinados.
> - Preview Interativo com legenda de níveis (🌎 N1, 📍 N2, 📂 N3, 🔍 N4).
> - Ícones e cores originais sincronizados com o novo Design System.

## Mudanças Propostas

### [Componente Frontend - Next.js]

#### [MODIFICAR] [globals.css](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/TM%20Pastas/tm-pastas-next/app/globals.css)
- Implementar os tokens do TM Hub para cores de fundo, bordas e sombras.
- Configurar fontes `Syne` (títulos) e `DM Sans` (leitura).

#### [MODIFICAR] [Componentes Individuais]
- **Header**: Logo TM oficial e navegação em estilo "capsule".
- **Wizard**: Adição de micro-interações no hover dos checkboxes e transições suaves no acordeão.
- **Interactive Preview (PreviewRow)**: Linhas com indicadores de nível coloridos, botões de ação (Mover/Adicionar/Remover) com design minimalista.
- **Footer**: Botões com gradientes "TM Emerald" e efeitos de profundidade.

## Plano de Verificação

### Verificação Manual
- Validar se a estrutura de indentação do preview reflete corretamente a hierarquia de pastas.
- Garantir que a legenda de níveis (N1-N4) no topo do preview esteja legível e fiel ao código.
- Conferir se o input de levantamento na barra de configuração segue o padrão de preenchimento do novo design.
