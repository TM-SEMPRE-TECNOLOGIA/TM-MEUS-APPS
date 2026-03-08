# Plano de Implementação — Atualização Visual TM Relatório SP

Refatorar o frontend do `TM Relatório SP` para adotar o Design System moderno e claro (Light Theme) do `TM Hub`.

## Revisão do Usuário Requerida

> [!IMPORTANT]
> O tema mudará de **Cyber-Dark (Escuro)** para **Modern-Light (Claro)**. Esta é uma mudança visual significativa para alinhar o aplicativo com a nova identidade do TM Hub.

## Mudanças Propostas

### [Componente Frontend]

#### [MODIFICAR] [globals.css](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/TM%20Relatorio%20SP/nextjs-frontend/app/globals.css)
- Remover variáveis do tema escuro e classes `@utility` legadas.
- Implementar os tokens de design do TM Hub (variáveis `--tm-*`).
- Configurar o novo fundo claro e a tipografia.

#### [MODIFICAR] [layout.tsx](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/TM%20Relatorio%20SP/nextjs-frontend/app/layout.tsx)
- Importar as fontes `Syne` e `DM Sans` do Google Fonts.
- Atualizar metadados se necessário.

#### [MODIFICAR] [page.tsx](file:///C:/Users/thiag/TM-MEUS-APPS/NEXT%20APPS/TM%20Relatorio%20SP/nextjs-frontend/app/page.tsx)
- Implementar a estrutura de **Sidebar (Barra Lateral)** para navegação entre etapas do processo (Configuração → Varredura → Geração).
- Adicionar **Breadcrumbs** no cabeçalho para indicar a posição atual no fluxo.
- Reorganizar o conteúdo em **Abas ou Seções Dinâmicas** baseadas na etapa ativa da sidebar.
- Adicionar um **Resumo de Estatísticas** (Imagens, Pastas, Status) acessível na interface.
- Implementar os ícones e estilos de "Estado da Etapa" (Ativo, Pendente, Concluído).
- **Preservar rigorosamente todo o estado e lógica de negócio existente.**

## Plano de Verificação

### Verificação Manual
- Executar o servidor de desenvolvimento Next.js e verificar:
    - O layout de **Sidebar** funciona corretamente para navegação.
    - O **Breadcrumb** atualiza conforme a etapa.
    - Os botões e inputs seguem o estilo refinado do redesign.
    - O fluxo de 3 etapas (Configuração, Varredura, Geração) está intuitivo.
    - Os logs estão legíveis e coloridos corretamente (Sucesso/Erro/Processamento).
    - Todos os fluxos funcionais (Escanear, Gerar, Baixar) permanecem operacionais.
