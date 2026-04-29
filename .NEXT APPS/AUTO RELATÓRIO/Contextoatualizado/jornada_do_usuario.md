# 🗺️ Jornada de Usuário do Ecossistema TM

## 🛠️ App 1: Gestión Admin (TM Ordens / Levantamento)
**Público:** Administradores e Supervisores.

1.  **Criação de OS:** Administrador cadastra uma nova OS no painel, definindo cliente, local e técnico responsável.
2.  **Distribuição:** Sistema gera um token único e envia o push via WhatsApp para o técnico encarregado.
3.  **Monitoramento:** Acompanha em tempo real o chat (WhatsApp Style) do técnico em campo.

## 📱 App 2: Interface de Campo (TM-OS)
**Público:** Técnicos e Vistoriadores.

1.  **Acesso:** Clica no link do WhatsApp e abre a OS sem necessidade de login complexo (autenticação via Token/WhatsApp).
2.  **Configuração Visual:** Seleciona onde está trabalhando (Área Externa > Jardim).
3.  **Captura Inteligente:**
    - Registra a **[Vista Ampla]**.
    - Escreve sobre o **[Serviço]** realizado diretamente no chat e clica para tirar foto.
    - Captura **[Detalhes]** específicos se houver algum erro ou observação.
4.  **Conclusão:** Finaliza a jornada. O sistema empacota os dados para o servidor.

## 📄 App 3: Gerador de Report (AutoRelatorioV1)
**Público:** Analistas e Backoffice.

1.  **Recepção:** Recebe as fotos já estruturadas em pastas:
    - `OS_123_CLIENTE/- Vista ampla/`
    - `OS_123_CLIENTE/01. Troca de Lampada/`
2.  **Processamento:** Dispara o `run.py` (Script Python).
3.  **Entrega:** Word final gerado com inteligência de layout (Premium) pronto para envio ao cliente.

---
### 🔗 Conexão de Ecossistema
- **Core:** SQL Centralizado (PostgreSQL/SQLite).
- **Backend Bridge:** FastAPI/Next.js integrados.
- **Relatórios:** Motor Python Legacy (Mantido para estabilidade e conformidade Word).
