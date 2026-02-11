# Gerador de Relatório Fotográfico (Local) — v2 (Modelos embutidos)

Este pacote roda **localmente no Windows** e gera um relatório Word a partir de uma **pasta raiz de fotos**, usando um **modelo DOCX** selecionável.

## Entradas
- **Pasta raiz (fotos)**: diretório com subpastas e imagens (`.jpg/.jpeg/.png`).
- **Modelo Word (DOCX)**: escolhido via ComboBox a partir da pasta `templates/`.
- **Pasta de saída**: onde serão salvos o DOCX final e os logs.

## Saídas
Na pasta de saída selecionada:
- `RELATÓRIO FOTOGRÁFICO - <NOME_DA_PASTA_RAIZ> - LEVANTAMENTO PREVENTIVO.docx`
- `process_log.txt`
- `erros_pastas.txt`

## Como usar (Windows)
1. Extraia esta pasta.
2. Duplo clique em `run_app.bat`.
3. No app:
   - selecione a **pasta raiz**
   - escolha um **modelo** no seletor (ComboBox)
   - selecione a **pasta de saída**
   - clique em **Pré-visualizar** (opcional, recomendado)
   - clique em **Gerar**

## Modelos
Os modelos embarcados ficam em `templates/`.
- Você pode adicionar novos modelos pelo botão **Adicionar modelo…** (ele copia o DOCX para `templates/`).

## Observações
- O modelo DOCX precisa conter a marca `{{start_here}}` para indicar o ponto de inserção das imagens.
