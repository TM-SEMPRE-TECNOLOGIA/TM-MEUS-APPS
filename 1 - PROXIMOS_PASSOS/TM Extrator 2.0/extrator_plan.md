# Plano de Implementação — Atualização Visual TM Extrator 2.0

Refatorar o frontend do `TM Extrator 2.0` para adotar o Design System **Ocean Breeze v2.0 (Light Theme)** extraído de `hub-ocean-breeze-v2.html`, padronizando a experiência do usuário com o restante dos aplicativos da suíte.

## Revisão do Usuário Requerida

> [!IMPORTANT]
> O aplicativo passará de um design "Ocean Breeze" para um layout de **Processo de 4 Etapas com Sidebar**, idêntico ao novo padrão do TM Relatório SP, garantindo consistência visual.

## Mudanças Propostas

### [Componente Frontend - Vite/React]

#### [MODIFICAR] [index.css](file:///C:/Users/thiag/TM-MEUS-APPS/TM%20Extrator%202.0/APP/src/index.css)
- Substituir variáveis antigas (`--TM-*`) pelos tokens oficiais do TM Hub (`--tm-*`).
- Remover estilos específicos do tema escuro/claro legado para usar o padrão unificado de alta performance e legibilidade.

#### [MODIFICAR] [App.jsx](file:///C:/Users/thiag/TM-MEUS-APPS/TM%20Extrator%202.0/APP/src/App.jsx)
- **Estruturação por Etapas**: O aplicativo será dividido em um fluxo guiado pela Sidebar:
    1.  **Upload (Envio)**: Foco exclusivo no dropzone e seleção do arquivo.
    2.  **Configuração (Extração)**: Escolha das regras de agregação e início do processamento.
    3.  **Preview (Conferência)**: Visualização dos itens extraídos, estatísticas e validação.
    4.  **Resultados (Download)**: Geração do XLSX consolidado e logs finais.
- **Cabeçalho com Breadcrumbs**: Adição da trilha de navegação dinâmica com o **Símbolo TM Oficial**.
- **Log System**: Melhoria na visualização dos logs, integrando-os na etapa final de Geração ou em um painel colapsável.
- **Preservação de Lógica**: A complexa lógica de parsing de DOCX (Regras de agregação, somas de itens e extração de memoriais) será mantida integralmente, mudando apenas como os resultados são exibidos.

## Plano de Verificação

### Verificação Manual
- Validar a navegação passo-a-passo no ambiente React.
- Testar a extração de um arquivo DOCX real e verificar se os dados no **Preview** estão corretos.
- Confirmar se o download do XLSX Consolidado/Memorial continua funcionando perfeitamente em todas as abas.
- Verificar a responsividade do layout da Sidebar.
