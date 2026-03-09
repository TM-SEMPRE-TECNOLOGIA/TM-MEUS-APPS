# 🚀 Plano Estratégico: TM HUB (SaaS Factory & Controle de Equipe)

Como seu sócio e parceiro de engenharia, analisei nossa base e o seu objetivo final. A verdadeira virada de chave para a TM - Sempre Tecnologia é sair de "um conjunto de ferramentas soltas" para uma **Plataforma Profissional Única**, onde o **TM HUB** é o cérebro operacional.

Abaixo está a visão ideal arquitetural e de negócios para alcançar esse padrão corporativo.

---

## 1. O Papel do TM HUB: O "Centro de Comando"

O TM HUB deixará de ser apenas uma tela de links e passará a ser um **Portal Administrativo (Backoffice) e um Portal de Usuários (Front-office)**.

### Visão do Admin (Você / Sócios / Gerentes):
- **Painel de Monitoramento (Analytics):** Você verá quais ferramentas a equipe mais usa, tempo gasto, erros gerados e volume de documentos processados.
- **Gestão de Usuários e Permissões:** O HUB controlará quem pode acessar o quê. (Exemplo: O *Usuário A* tem acesso apenas ao TM Extrator, enquanto o *Usuário B* tem acesso ao Relatório SP e ao TM Comparador).
- **Log de Acessos e Auditoria:** Rastreabilidade completa do que foi feito.

### Visão da Equipe (Usuários):
- Ao fazer login, a equipe vê uma interface limpa (`Ocean Breeze Light`), apenas com as ferramentas que lhes foram designadas.
- **Single Sign-On (SSO):** O login feito no HUB autentica automaticamente em todas as outras ferramentas do ecossistema (Pastas, Ordens, Gerenciador). Não há mais logins repetidos.

---

## 2. A Comunicação Entre os Aplicativos (O Ecossistema)

Atualmente, os aplicativos rodam isolados. O cenário "SaaS Ideal" exige que eles conversem entre si. Como isso funcionará na prática?

### 🔄 Fluxo Ideal Integrado:
1. **TM HUB (A Entrada):** O usuário loga. O HUB fornece o *Token de Autenticação* global e injeta os dados do usuário.
2. **TM Pastas (A Base):** Antes de iniciar um trabalho, o usuário usa o TM Pastas pelo HUB para gerar a estrutura de diretórios do cliente X aprovado.
3. **TM Ordens (O Gatilho):** O gerente no HUB emite uma Ordem de Serviço (OS).
4. **TM Gerenciador (O Motor):** A OS cai no Gerenciador, onde o analista vê a tarefa em uma esteira (Kanban).
5. **Ferramentas Específicas (A Execução):**
   - Se a tarefa for comparar preços: O usuário clica na OS e o sistema abre o **TM Comparador**, já carregado com os dados do cliente.
   - Se for relatório do governo: Abre o **TM Relatório SP**.
   - Se precisar ler pdfs complexos: Usa o **TM Extrator 2.0**.

### 🧩 Como eles "Falam" Tecnicamente?
Para funcionar assim de forma profissional, precisaremos de:
- **Uma API Central ou Banco de Dados Compartilhado:** Um banco PostgreSQL ou Supabase/Firebase onde todos os aplicativos leem os mesmos dados de Clientes e OS.
- **Contexto Compartilhado:** O "estado" do sistema viaja pelas URLs ou via API (ex: `hub.tm/comparador?cliente_id=123`).

---

## 3. Plano de Ação para Implementação Equipe (Professional Step-by-Step)

Para profissionalizar o uso interno e se preparar para vender como SaaS externo no futuro, devemos seguir estas etapas:

### 🏆 Fase 1: Fundação e Core (Onde estamos)
- [x] Unificação Visual (Aplicar o Design System Light em todos).
- [ ] Transformar o TM HUB (*Next.js*) em uma casca que não só redireciona, mas valida quem está acessando.
- [ ] Criar no TM HUB um "Mock" (Simulação) de tela de Dashboard de Sócios (Gráficos, Atividade Direta).

### 🔒 Fase 2: Autenticação Global (SSO)
- [ ] Implementar um sistema de Auth (Ex: *NextAuth* / *Clerk* / *Supabase*).
- [ ] Conectar os 6 aplicativos ao mesmo provedor de login do HUB.

### 📊 Fase 3: Dashboard de Gestão (Monitoramento)
- [ ] Construir a aba "Admin" que só você tem acesso.
- [ ] Criar tabelas e gráficos em tempo real mostrando os relatórios gerados por sua equipe nos apps satélites.
- [ ] Bloqueio/Desbloqueio de ferramentas por usuário via painel.

### 🌐 Fase 4: Banco de Dados Central
- [ ] Tirar os dados "chumbados" e arquivos JSON locais de dentro das ferramentas.
- [ ] Fazer todas as ferramentas gravarem logs de uso no Banco de Dados Central para o HUB ler e mostrar nos gráficos.

---

## 💡 Uma sugestão de Negócio

Tratando isso como **produto**, o HUB se torna o produto que gerencia "Micro SaaS" (apps). Com a arquitetura separada em Next.js (já planejada no `MASTER_PLAN_360.md`), no futuro, a TM pode vender assinaturas. 
*Ex: O escritório de engenharia X quer pagar apenas pelo "TM Extrator 2.0". Você cria no HUB um acesso de cliente que libera só essa ferramenta, com quota mensal.*

Nós temos toda a base para isso. Apenas precisamos finalizar a padronização visual e colocar o motor do HUB central para orquestrar tudo.
