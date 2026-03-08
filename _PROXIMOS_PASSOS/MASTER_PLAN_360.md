## 💎 A Visão "SaaS Factory" (MANUS)
Conforme extraído dos documentos estratégicos em `MANUS`, a TM não é mais apenas uma coleção de scripts, mas uma **Fábrica de Software como Serviço**.

### Objetivos Estratégicos:
- **Fim das "Ilhas Digital"**: Unificar apps que hoje vivem em portas e designs diferentes.
- **Modelo iLovePDF**: Um portal central onde o usuário encontra tudo, com UX coesa e profissional.
- **Monetização e Escala**: Preparar a arquitetura (Next.js 16 + FastAPI) para suportar múltiplos módulos e usuários.

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
Tendo em vista os arquivos em `_PROXIMOS_PASSOS` e os 6 apps centrais totalmente prontos agora, a ordem recomendada de aplicação de código (Next.js/Tailwind) para a SaaS UI:
- [ ] Construir Fundação Base: **TM Hub** (Next.js 16).
- [ ] Aplicar *Redesign* no **TM Comparador** (Usa framework base Next.js já estruturado).
- [ ] Aplicar *Redesign* no **TM Relatório** (Padrão).
- [ ] Aplicar *Redesign* no **TM Pastas**.
- [ ] Aplicar *Redesign* no **TM Ordens**.
- [ ] Aplicar *Redesign* no **TM Extrator 2.0** (Migração e Update Visual conjuntos).
- [ ] Aplicar *Redesign* no **TM Relatório SP**.
- [ ] Aplicar *Redesign* no **G-2**.
