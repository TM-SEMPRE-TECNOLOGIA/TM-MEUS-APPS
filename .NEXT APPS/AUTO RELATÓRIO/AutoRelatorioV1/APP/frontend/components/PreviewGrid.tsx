"use client";

import { LayoutGrid, MapPin, Eye, Paintbrush, Info, Target } from 'lucide-react';
import { motion } from 'framer-motion';

interface PreviewGridProps {
  conteudo: any[] | null;
  apiUrl: string;
}

export default function PreviewGrid({ conteudo, apiUrl }: PreviewGridProps) {
  
  // Função para limpar o texto de marcadores técnicos desnecessários
  const cleanCategoryText = (text: string) => {
    return text
      .replace(/»/g, '') // Remove setas
      .replace(/^\s*[\-\d]+\s*-\s*/, '') // Remove números e traços iniciais (ex: "1 - ", "»- ")
      .replace(/^- /, '') // Remove traços isolados
      .trim();
  };

  // Função para mapear ícones baseada em palavras-chave (mais sóbria)
  const getIconForText = (text: string) => {
    const clean = text.toLowerCase();
    if (clean.includes('área')) return <MapPin size={14} className="text-brand-primary/80" />;
    if (clean.includes('vista') || clean.includes('ampla')) return <Eye size={14} className="text-slate-400" />;
    if (clean.includes('pintura')) return <Paintbrush size={14} className="text-slate-400" />;
    if (clean.includes('medição') || clean.includes('total')) return <Target size={14} className="text-brand-primary/60" />;
    return <div className="w-1 h-1 rounded-full bg-slate-300" />;
  };

  return (
    <div className={`glass-panel flex flex-col relative overflow-hidden bg-white transition-all duration-500 ${!conteudo ? 'h-[425px]' : 'flex-1 min-h-[425px]'}`}>
      <div className="px-8 py-4 border-b border-brand-primary/10 flex items-center justify-between bg-slate-50/50">
        <div className="flex items-center gap-3">
          <div className="w-6 h-6 flex items-center justify-center text-brand-primary">
            <LayoutGrid size={16} strokeWidth={2} />
          </div>
          <h3 className="font-bold text-[13px] text-slate-700 uppercase tracking-wide">Visualização da Estrutura</h3>
        </div>
        <div className="flex gap-1.5">
           <div className="w-2 h-2 rounded-full bg-slate-300" />
           <div className="w-2 h-2 rounded-full bg-slate-300" />
           <div className="w-2 h-2 rounded-full bg-slate-300" />
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-8 custom-scrollbar">
        {conteudo && conteudo.length > 0 ? (
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-6">
             {conteudo.map((item: any, idx: number) => {
               const isString = typeof item === 'string';
               const isObject = typeof item === 'object' && item !== null;
               const imgPath = isObject ? (item.imagem || item.imagem_fachada) : null;
               const descText = isObject ? item.texto_descricao : null;
               const tableData = isObject ? item.tabela_medicao : null;
               const detailText = isObject ? item.texto_padrao : null;
               
               if (imgPath) {
                 const isFachada = !!item.imagem_fachada;
                 return (
                   <motion.div 
                    key={idx} 
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    className={`relative aspect-square rounded-lg border-2 overflow-hidden bg-slate-50 transition-all hover:ring-2 hover:ring-brand-primary/20 group ${isFachada ? 'border-brand-primary shadow-sm' : 'border-slate-200'}`}
                   >
                     <img 
                      src={`${apiUrl}/api/thumbnail?path=${encodeURIComponent(imgPath)}`} 
                      className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" 
                      alt="Preview"
                     />
                     {isFachada && (
                       <div className="absolute top-2 left-2 bg-brand-primary text-white text-[8px] font-black px-2 py-0.5 rounded shadow-lg uppercase tracking-wider">
                         Fachada
                       </div>
                     )}
                   </motion.div>
                 );
               } else if (isString) {
                  const isSub = item.includes('»');
                  const cleanItem = cleanCategoryText(item);
                  return (
                    <div key={idx} className={`col-span-full py-4 mt-8 first:mt-0 flex items-center gap-4 ${isSub ? 'pl-8' : ''}`}>
                       <div className="flex items-center gap-3">
                         {getIconForText(item)}
                         <span className={`font-black uppercase tracking-[0.2em] ${isSub ? 'text-[11px] text-slate-400' : 'text-[14px] text-slate-800'}`}>
                           {cleanItem}
                         </span>
                       </div>
                       <div className="h-[2px] flex-1 bg-gradient-to-r from-slate-100 to-transparent rounded-full" />
                    </div>
                  );
               } else if (descText) {
                  return (
                    <div key={idx} className="col-span-full py-5 px-6 bg-slate-50 border-l-4 border-brand-accent my-4 text-slate-700 font-medium text-[13px] leading-relaxed pr-12 relative rounded-r-lg shadow-sm">
                        <div className="absolute right-6 top-6 text-brand-accent/30"><Info size={20} /></div>
                        "{descText.replace(/<RED>|<\/RED>/g, '')}"
                    </div>
                  );
               } else if (tableData) {
                  return (
                    <div key={idx} className="col-span-full md:col-span-4 lg:col-span-3 py-5 px-6 bg-brand-primary text-white rounded-xl flex items-center justify-between border border-brand-secondary my-4">
                       <div className="flex flex-col">
                          <span className="text-[9px] font-black uppercase tracking-[0.25em] opacity-60 mb-1">Medição Estimada</span>
                          <span className="text-[14px] font-black uppercase tracking-widest">{tableData.tipo === 'pintura' ? 'Consumo de Pintura' : 'Mobília'}</span>
                       </div>
                       <div className="flex gap-3">
                          {tableData.medidas.map((m: any, midx: number) => (
                             <div key={midx} className="bg-white/10 px-4 py-2 rounded-xl backdrop-blur-md border border-white/10 flex flex-col items-center">
                                <span className="text-[14px] font-black">{m.total ? `${m.total.toFixed(1)}m²` : m.total_un ? `${m.total_un}UN` : ''}</span>
                                <span className="text-[8px] font-bold uppercase opacity-60 leading-none">{m.nome?.split('_').pop() ?? ''}</span>
                             </div>
                          ))}
                       </div>
                    </div>
                  );
               } else if (detailText) {
                  return (
                    <div key={idx} className="col-span-full py-3 mt-10 flex items-center justify-center bg-slate-800 rounded-lg border border-slate-700 overflow-hidden relative group">
                       <div className="absolute inset-0 bg-gradient-to-r from-brand-primary/20 to-brand-secondary/20 opacity-0 group-hover:opacity-100 transition-opacity" />
                       <span className="text-[13px] font-black text-white uppercase tracking-[0.4em] relative z-10">{detailText}</span>
                    </div>
                  );
               }
               return null;
             })}
          </div>
        ) : (
          <div className="h-full flex flex-col items-center justify-center text-center py-4">
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="w-16 h-16 rounded-full flex items-center justify-center mb-4 border-2 border-dashed border-slate-200"
            >
              <LayoutGrid size={24} className="text-slate-300" strokeWidth={1.5} />
            </motion.div>
            <h4 className="text-[14px] font-black text-slate-700 mb-2 uppercase tracking-wide">Aguardando Análise</h4>
            <p className="text-[11px] text-slate-400 max-w-xs leading-relaxed font-medium">
              Insira o diretório raiz e clique em configurar para que o motor possa mapear a árvore de arquivos do projeto e gerar a prévia estrutural.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
