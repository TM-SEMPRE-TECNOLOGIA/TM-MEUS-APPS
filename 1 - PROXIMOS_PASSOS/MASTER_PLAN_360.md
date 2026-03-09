## 💎 A Visão "SaaS Factory" (MANUS)
Conforme extraído dos documentos estratégicos em `MANUS`, a TM não é mais apenas uma coleção de scripts, mas uma **Fábrica de Software como Serviço**.

### Objetivos Estratégicos:
- **Fim das "Ilhas Digital"**: Unificar apps que hoje vivem em portas e designs diferentes.
- **Modelo iLovePDF**: Um portal central onde o usuário encontra tudo, com UX coesa e profissional.
- **Migração para Next.js 16**: Foco total em modernização. Todo o ecossistema será migrado para Next.js. Consulte o `roadmap_migracao_tecnologia.md` para as prioridades.

---

## 🔍 Status de Organização (360º)

| App | Organização de Pastas | Estado Visual | Próximo Passo |
|-----|-----------------------|---------------|---------------|
| **TM Hub (Core)** | 🔴 Apenas Mockup HTML | ☀️ Light | **Implementar Next.js Hub** |
| **TM Extrator 2.0** | ✅ APP/DEV/DOCS | 🌑 Dark | Migrar p/ Next.js Light |
| **TM Extrator (v1)** | ✅ APP/DEV/LEGADO | 🌑 Dark | Incorporar ao Core 2.0 |
| **TM Relatorio SP** | 🟡 Parcial | 🌑 Dark | Padronizar pastas e Light UI |
| **TM Central** | ❓ Localizando | 🌑 Dark | Mover p/ NEXT APPS |
| **LICITUS_BOT** | 🟡 Na Raiz | 🌑 Dark | Mover p/ NEXT APPS |
| **TM Pastas** | 🔵 Next.js | 🌑 Dark | Update para Light |
| **TM Comparador** | 🔵 Next.js | 🌑 Dark | Update para Light |
| **TM Ordens** | 🔵 Next.js | 🌑 Dark | Update para Light |
| **G-2 (Maffeng)** | 🔴 Vite | ☀️ Light | **Migrar React -> Next.js** |
| **Bot Chat** | 🔴 Sem Design | ❌ None | Aplicar Design System |

---

## 🎨 Plano Mestre de Refatoração de Design (SaaS UI)

O objetivo principal desta fase é garantir que **todos os aplicativos TM possuam o Design System Light**, unificado e focado na usabilidade de ponta. Foram consolidados no diretório `_PROXIMOS_PASSOS` os planos base e previews de cada um. 

### 📁 Status de Atualizações Pendentes em `_PROXIMOS_PASSOS`

Realizei uma varredura completa nas pastas movimentadas. O status atual de Planejamento e Preview para cada app é:

| Aplicativo | Arquivo de Plano | Arquivo de Preview HTML | Status Atual |
|------------|------------------|-------------------------|--------------|
| **G-2 (Maffeng)** | ✅ `g2_plan.md` | ✅ `g2_preview.html` | Pronto p/ Refatoração |
| **TM Comparador** | ✅ `comparador_plan.md` | ✅ `comparador_preview.html` | Pronto p/ Refatoração |
| **TM Extrator 2.0**| ✅ `extrator_plan.md` | ✅ `extrator_preview.html` | Pronto p/ Refatoração |
| **TM Ordens** | ✅ `ordens_plan.md` | ✅ `ordens_preview.html` | Pronto p/ Refatoração |
| **TM Pastas** | ✅ `pastas_plan.md` | ✅ `pastas_preview.html` | Pronto p/ Refatoração |
| **TM Relatório SP**| ✅ `implementation_plan.md`| ✅ `preview.html` | Pronto p/ Refatoração |
| **TM Relatório** (Padrão)| ✅ `relatorio_plan.md` | ✅ `relatorio_preview.html` | Pronto p/ Refatoração |

*(Nota: Os aplicativos marcados como "Pronto" já possuem uma prévia visual mapeada e o plano técnico gerados, todos concentrados fisicamente em `_PROXIMOS_PASSOS`. Apps como Licitus Bot e Studio Relatório foram permanentemente arquivados/isolados das dependências unificadas do HUB)*

---

## 🎯 Próximos Passos (Imediato)

### 1. Unificação Geográfica (Pastas)
- [x] **Sincronizar Commits**: Feito!
- [x] **Mover LICITUS_BOT**: Isolado para `projeto licitus` na raiz, removido da lógica 360.
- [x] **Localizar TM Central e Studio Relatório**: Transformados em legado (apagados da esteira do HUB principal).
- [x] **Consolidar Rascunhos**: Feitos para todos os 6 aplicativos centrais do Hub.

### 2. Execução da Refatoração de Design (Ordem Recomendada)
Tendo em vista o `roadmap_atualizacao_visual.md` recém gerado e a priorização requerida, a ordem de aplicação para a integração do **Ocean Breeze v2.0 (Light)** é:
- [ ] 1. **TM Relatório SP** (Fluxo de Etapas com Sidebar Light).
- [ ] 2. **TM Pastas** (Padrão Light Interativo).
- [ ] 3. **TM Extrator 2.0** (Fluxo guiado via Sidebar Light).
- [ ] 4. Construir Fundação Base: **TM Hub / DEV HUB** (Baseando-se no `hub-ocean-breeze-v2.html`).
- [ ] 5. Aplicar *Redesign* no **TM Comparador**.
- [ ] 6. Aplicar *Redesign* no **TM Relatório** (Padrão).
- [ ] 7. Aplicar *Redesign* no **TM Ordens**.
- [ ] 8. Aplicar *Redesign* no **G-2**.
