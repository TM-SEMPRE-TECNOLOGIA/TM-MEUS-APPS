# 🧭 Análise Geral do Repositório: TM-MEUS-APPS

Este documento apresenta uma análise detalhada da arquitetura, padronização, ecossistema de aplicativos e próximos passos dentro do repositório raiz `TM-MEUS-APPS` da "TM - Sempre Tecnologia".

---

## 🏗️ 1. Visão Arquitetural e Estrutura Principal

O repositório opera como um grande **Monorepo / "SaaS Factory"** (Fábrica de Software como Serviço), que centraliza todos os sistemas, integrações, documentações de design e scripts antigos da empresa. A transição atual foca em extinguir "ilhas digitais" (aplicativos isolados) para criar uma plataforma unificada (Hub) no estilo de grandes portais SaaS (ex: iLovePDF), com uma UX coesa, profissional e primariamente desenvolvida em **Next.js**.

**Diretórios Raiz Principais:**
- `0 - NEXT APPS`: O coração de desenvolvimento ativo. Contém as aplicações modernas recém reformuladas ou em processo.
- `1 - PROXIMOS_PASSOS`: Central estratégica de planejamento. Armazena mapas mentais, roadmaps técnicos de migração de versões e o "MASTER PLAN 360", que dita o norte do repositório.
- `Design System TM`: Fonte única da verdade para UI/UX. Hospeda referências visuais estáticas (Ocean Breeze v2.0), catálogos de componentes e a fundação de estilos que todas as outras aplicações devem espelhar.
- `LEGADO - ANTIGOS`: Abastece o histórico e abriga versões V1/arquivos mortos para retrocompatibilidade ou cópia de lógicas de negócio antigas.
- `MEUS COMMITS`: Um diretório central para auditoria. Garante a regra rigorosa da "linha do tempo" da TM de espelhar as atualizações de todos os apps em um só lugar.
- `projeto licitus`: Projeto à parte, desenvolvido especificamente para um cliente. Contém scripts documentais, e funciona de forma independente do ecossistema central SaaS da TM.

---

## 🚀 2. Ecossistema de Aplicações (`0 - NEXT APPS` e correlatos)

Esta pasta detém as principais ferramentas de negócio, na maioria já portadas ou em portabilidade para React / Next.js com TypeScript:

1. **DEV HUB / TM HUB:** 
   - *Status*: Core System (Centralizador). Em refatoração para servir de fundação base para todas as micro-aplicações do ecossistema.
2. **TM Comparador:**
   - *Finalidade*: Ferramenta pesada de comparação de propostas/contratos e dados dispostos em formato de grid.
   - *Status:* Já em Next.js, listado para receber atualização do "Design Light Interativo".
3. **TM Extrator & TM Extrator 2.0:**
   - *Finalidade*: Robôs / Ferramentas de extração de dados e automação documental. A v2 separa responsabilidades entre Web (Interface) e Engine local/Rápido.
4. **TM Gerenciador:**
   - *Finalidade*: Complexo sistema de gestão de esteiras, sendo um dos maiores projetos (mais de 160 componentes/módulos), atuando possivelmente como um Mini-ERP da empresa.
5. **TM Ordens:**
   - *Finalidade*: Sistema utilitário para formulação e disparo de Ordens de Serviço.
6. **TM Pastas:**
   - *Finalidade*: Automatizador de estrutura de arquivos (diretórios padronizados para licitações e afins).
7. **TM Relatório / TM Relatório SP:**
   - *Finalidade*: Ferramentas exclusivas para geração de relatórios fotográficos ou técnicos de engenharia. A versão "SP" atua diretamente nas regras do Contrato 0908 (Sabesp/Governo).
8. **G-2 (Maffeng):**
   - *Finalidade*: Dashboard analítico, KPIs, mapas de calor interativos e gestão de ordens em mapa.
   - *Status*: Em migração de arquitetura (Vite/React para Next.js).

---

## 🎨 3. Padrões de Qualidade (Quality Assurance & Design)

- **Regra de "Dupla Atualização de Commits"**: A TM adota um mecanismo rígido onde **qualquer** alteração em aplicação deve gerar um arquivo HTML visualmente agradável de "Log de Atualização" (arquivo `commit.html`). Esse arquivo fica no app e uma cópia exata fica em `MEUS COMMITS/PADRÃO LINHA DO TEMPO`. O layout é padronizado (Dark Mode com tipografia Lora/DM Sans) visando relatórios entregáveis e bonitos sem precisar acessar terminais Git.
- **Design System Obrigatório ("Ocean Breeze")**: Uma rigidez imensa de estética, rejeitando componentes ad-hoc e exigindo que tudo emita a percepção "Premium". A paleta, os `border-radius`, os ícones `Lucide/Phosphor` devem ser unificados em todos os sistemas. Atualmente há um movimento de migrar do `Dark Mode` generalizado para o novo `Light Model (Ocean Breeze v2)`.

---

## 🎯 4. Status de Refatoração e Próximos Passos ("Master Plan 360")

De acordo com o `MASTER_PLAN_360.md`, o repositório está no meio de sua maior transição arquitetural. 

**Objetivos Focais Imediatos da TM:**
1. **Unificação Geográfica**: Concluída. Aplicativos isolados como "Studio Relatório" ou "Licitus Bot" foram separados, enquanto os 6-7 núcleos principais orbitam em torno do Hub.
2. **Migração de Tecnologia Geral para Next.js 16**.
3. **Refatoração UI/UX Completa da Interface "Dark" p/ "Light" guiada pelo Design System**.

**A Ordem de Execução do Roadmap Atual:**
1. _TM Relatório SP_ (Refatoração de UI Light com Sidebar).
2. _TM Pastas_ (Design Tático Light Interativo).
3. _TM Extrator 2.0_ (Integração Total Engine + UI UI Light).
4. _Fundação DEV HUB_ (Portal principal conectando os apps).
5. _G-2 / Outros_ (Migração de roteamento + Re-skin completo).

## 💡 Resumo Conclusivo
O repositório `TM-MEUS-APPS` se encontra altamente regulado e maduro do ponto de vista de procedimentos operacionais de front-end. Nota-se um alto rigor metodológico (rastreabilidade duplicada de commits via UI) e uma obsessão por coesão visual. A base de código está num momento estratégico de se "libertar" dos componentes antigos disjuntos ("Ilhas Digitais") e se consolidar como uma verdadeira e única "SaaS Factory", com quase todo seu core hospedado em Next.js.
