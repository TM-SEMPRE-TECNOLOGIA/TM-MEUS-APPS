# TM Central AI Workflow

> **Este arquivo deve ser lido por qualquer Agente de IA antes de iniciar trabalhos neste repositório.**

## 1. Princípios do Projeto
Este repositório (`TM Central`) atua como o Hub central do ecossistema de aplicativos do usuário.
-   **Estética:** Cosmic Theme (Dark Mode, Glassmorphism, Gradientes lineares).
-   **Tecnologia:** HTML5, CSS3 (Sem frameworks pesados), Vanilla JS.
-   **Persistência:** `localStorage` para dados de usuário (commits, tarefas).

## 2. Regras de Ouro
Ao realizar qualquer alteração, o Agente deve seguir este checklist:

### A. Registro de Atividades (CRÍTICO)
1.  **Commits HTML:** Ao finalizar QUALQUER tarefa (feature, fix, refactor), é **OBRIGATÓRIO** adicionar uma entrada no arquivo `commit.html` antes de notificar o usuário.
    -   **Onde editar:** No array `baseCommits` dentro da tag `<script>` do `commit.html`.
    -   **Formato:** `{ id: Date.now(), type: 'feature', message: 'Título curto', description: 'Detalhes...', files: [...] }`
    -   **Regra de Ouro:** "Se não está no `commit.html`, não aconteceu."

2.  **Roadmap:** Se estiver criando uma feature nova:
    -   Verifique `roadmap.html`.
    -   Adicione o card na coluna "In Progress" ou "Done".

### B. Padrões de Código
-   **CSS:** Não crie estilos inline. Use as variáveis CSS definidas em `padroes.html` (ou copie de lá).
    -   `var(--bg-primary)`, `var(--accent-blue)`, etc.
-   **Ícones:** Use emojis ou SVGs simples; evite carregar bibliotecas externas pesadas (FontAwesome) a menos que já existam.
-   **Navegação:** Todo arquivo HTML deve ter um botão "Voltar" apontando para `Readme.html` ou para o Hub anterior.

## 3. Estrutura de Pastas
-   `/TM Central`: Hub principal.
-   `/TM Pastas`: App Python (Gerador de Pastas).
-   `/TM Demandas`: App React (Gestão de Tarefas).
-   ... (respeite a estrutura existente).

## 4. Atualização de Links
Se criar um novo arquivo `.html`:
1.  Adicione-o ao `Readme.html` (na seção Quick Links ou como um novo Card).
2.  Garanta que ele siga o `padroes.html`.
