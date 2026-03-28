"use client";

import { motion, AnimatePresence } from 'framer-motion';
import { FolderOpen, Play, ChevronDown, ChevronUp, FileText, Settings, Eye } from 'lucide-react';

interface SidebarWizardProps {
  activeStep: number;
  setActiveStep: (step: number) => void;
  tipoRelatorio: string;
  setTipoRelatorio: (type: string) => void;
  pastaRaiz: string;
  selectFolder: (type: 'raiz' | 'saida') => void;
  modeloSelecionado: string;
  setModeloSelecionado: (model: string) => void;
  templates: string[];
  fetchTemplates: () => void;
  selectedDescription: string;
  setSelectedDescription: (desc: string) => void;
  descriptionsOptions: { id: string; label: string }[];
  handleScan: () => void;
  handleGenerate: () => void;
  loading: boolean;
  isGenerating: boolean;
  hasConteudo: boolean;
}

export default function SidebarWizard({
  activeStep,
  setActiveStep,
  tipoRelatorio,
  setTipoRelatorio,
  pastaRaiz,
  selectFolder,
  modeloSelecionado,
  setModeloSelecionado,
  templates,
  fetchTemplates,
  selectedDescription,
  setSelectedDescription,
  descriptionsOptions,
  handleScan,
  handleGenerate,
  loading,
  isGenerating,
  hasConteudo
}: SidebarWizardProps) {
  
  const steps = [
    {
      id: 1,
      isLocked: false,
      title: "Diretório Raiz",
      subtitle: "CONFIGURAÇÃO DE ORIGEM",
      icon: <div className="w-8 h-8 rounded-full bg-brand-primary flex items-center justify-center text-white text-xs font-bold">01</div>,
      content: (
        <div className="space-y-6 pt-2">
          <div>
            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-3 block">Modo de Organização</label>
            <div className="flex gap-1 bg-slate-100 p-1 rounded-lg">
              <button
                onClick={(e) => { e.stopPropagation(); setTipoRelatorio('tradicional'); }}
                className={`flex-1 py-2 px-3 text-[11px] font-bold rounded-md transition-all ${tipoRelatorio === 'tradicional' ? 'bg-white text-brand-secondary shadow-sm' : 'text-slate-500 hover:text-slate-700'}`}
              >
                Tradicional
              </button>
              <button
                onClick={(e) => { e.stopPropagation(); setTipoRelatorio('sp'); }}
                className={`flex-1 py-2 px-3 text-[11px] font-bold rounded-md transition-all ${tipoRelatorio === 'sp' ? 'bg-white text-brand-secondary shadow-sm' : 'text-slate-500 hover:text-slate-700'}`}
              >
                Organizado SP
              </button>
            </div>
          </div>
          
          <div>
            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-3 block">Caminho do Diretório</label>
            <div className="relative group">
              <input
                type="text"
                value={pastaRaiz}
                placeholder="C:\Users\Admin\Documents\Project"
                readOnly
                className="input-field text-xs h-11 pr-10 border-slate-200"
              />
              <button 
                onClick={(e) => { e.stopPropagation(); selectFolder('raiz'); }}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-brand-primary hover:text-brand-secondary transition-colors"
              >
                 <FolderOpen size={16} />
              </button>
            </div>
          </div>

          <button
            onClick={(e) => { e.stopPropagation(); selectFolder('raiz'); }}
            className="btn-primary w-full py-4 text-xs font-black uppercase tracking-widest bg-brand-primary hover:bg-brand-secondary shadow-brand-primary/20"
          >
            Configurar Origem
          </button>
          
          <button
            onClick={(e) => { e.stopPropagation(); handleScan(); }}
            disabled={!pastaRaiz || loading}
            className={`btn-secondary w-full py-4 text-xs font-black uppercase tracking-widest border-2 border-brand-primary/20 text-brand-secondary hover:bg-slate-100 mt-2 ${!pastaRaiz ? 'opacity-30' : ''}`}
          >
            {loading ? 'Escaneando...' : 'Iniciar Varredura'}
          </button>
        </div>
      )
    },
    {
      id: 2,
      isLocked: !hasConteudo,
      title: "Modelo DOCX",
      subtitle: "PRÓXIMA ETAPA",
      icon: <div className={`w-8 h-8 rounded-lg flex items-center justify-center transition-colors ${!hasConteudo ? 'bg-slate-100 text-slate-300' : 'bg-brand-primary/10 text-brand-primary'}`}><FileText size={16} /></div>,
      content: (
        <div className="space-y-4 pt-4 border-t border-slate-100">
          <select
            className="w-full h-11 px-3 text-xs bg-slate-50 border border-slate-200 rounded-lg outline-none focus:bg-white focus:border-brand-primary focus:ring-4 focus:ring-brand-primary/10 transition-all font-bold text-slate-700 cursor-pointer appearance-none shadow-sm"
            style={{ backgroundImage: `url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%2364748b' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e")`, backgroundPosition: 'right 0.5rem center', backgroundRepeat: 'no-repeat', backgroundSize: '1.5em 1.5em', paddingRight: '2.5rem' }}
            value={modeloSelecionado}
            onChange={(e) => setModeloSelecionado(e.target.value)}
          >
            <option value="" disabled>Escolha um modelo...</option>
            {templates.map(t => <option key={t} value={t}>{t}</option>)}
          </select>
          <button
            onClick={(e) => { e.stopPropagation(); fetchTemplates(); }}
            className="btn-secondary w-full py-2 text-[10px] font-black uppercase"
          >
            Atualizar Lista
          </button>
        </div>
      )
    },
    {
      id: 3,
      isLocked: !hasConteudo || !modeloSelecionado,
      title: "Parâmetros",
      subtitle: "CONFIGURAÇÕES ADICIONAIS",
      icon: <div className={`w-8 h-8 rounded-lg flex items-center justify-center transition-colors ${!hasConteudo || !modeloSelecionado ? 'bg-slate-100 text-slate-300' : 'bg-brand-primary/10 text-brand-primary'}`}><Settings size={16} /></div>,
      content: (
        <div className="space-y-4 pt-4 border-t border-slate-100">
          <select
            className="w-full h-11 px-3 text-xs bg-slate-50 border border-slate-200 rounded-lg outline-none focus:bg-white focus:border-brand-primary focus:ring-4 focus:ring-brand-primary/10 transition-all font-bold text-slate-700 cursor-pointer appearance-none shadow-sm"
            style={{ backgroundImage: `url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%2364748b' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e")`, backgroundPosition: 'right 0.5rem center', backgroundRepeat: 'no-repeat', backgroundSize: '1.5em 1.5em', paddingRight: '2.5rem' }}
            value={selectedDescription}
            onChange={(e) => setSelectedDescription(e.target.value)}
          >
            {descriptionsOptions.map(opt => <option key={opt.id} value={opt.id}>{opt.label}</option>)}
          </select>
        </div>
      )
    },
    {
      id: 4,
      isLocked: !hasConteudo || !modeloSelecionado,
      title: "Visualização",
      subtitle: "RESULTADO FINAL",
      icon: <div className={`w-8 h-8 rounded-lg flex items-center justify-center transition-colors ${!hasConteudo || !modeloSelecionado ? 'bg-slate-100 text-slate-300' : 'bg-brand-primary/10 text-brand-primary'}`}><Eye size={16} /></div>,
      content: (
        <div className="space-y-4 pt-4 border-t border-slate-100">
          <button
            onClick={(e) => { e.stopPropagation(); handleGenerate(); }}
            disabled={isGenerating || !hasConteudo}
            className={`btn-primary w-full py-4 text-xs font-black uppercase tracking-widest hover:bg-brand-secondary shadow-brand-primary/20 ${!hasConteudo ? 'opacity-30 grayscale cursor-not-allowed' : ''}`}
          >
            Gerar Relatório
          </button>
        </div>
      )
    }
  ];

  return (
    <aside className="lg:col-span-4 xl:col-span-3 flex flex-col gap-3 h-full overflow-y-auto pr-2 custom-scrollbar pb-20 lg:pb-0">
      {steps.map((step) => (
        <motion.div
          key={step.id}
          layout
          onClick={() => !step.isLocked && setActiveStep(activeStep === step.id ? 0 : step.id)}
          className={`premium-card p-5 border-2 transition-all duration-400 ${
            step.isLocked 
              ? 'opacity-40 grayscale pointer-events-none border-transparent bg-slate-50/40' 
              : activeStep === step.id 
                ? 'border-brand-primary/30 bg-white ring-2 ring-brand-primary/5 shadow-md cursor-default' 
                : 'border-transparent bg-slate-50/80 hover:bg-white cursor-pointer hover:shadow-sm'
          }`}
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              {step.icon}
              <div>
                <h3 className="text-[13px] font-bold text-slate-700 uppercase tracking-tight">{step.title}</h3>
                <p className="text-[9px] text-slate-400 font-bold uppercase tracking-wider">{step.subtitle}</p>
              </div>
            </div>
          </div>
          
          <AnimatePresence>
            {activeStep === step.id && (
              <motion.div 
                initial={{ opacity: 0, height: 0, marginTop: 0 }} 
                animate={{ opacity: 1, height: 'auto', marginTop: 24 }} 
                exit={{ opacity: 0, height: 0, marginTop: 0 }}
                className="overflow-hidden"
                onClick={(e) => e.stopPropagation()} // Impede fechar ao clicar nos inputs/botões
              >
                {step.content}
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      ))}
      
    </aside>
  );
}

