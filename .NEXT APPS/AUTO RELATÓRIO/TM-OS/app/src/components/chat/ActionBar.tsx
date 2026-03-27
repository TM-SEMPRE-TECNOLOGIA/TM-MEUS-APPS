import React from 'react';
import { Camera, PenTool, Layout, Image } from 'lucide-react';

interface ActionBarProps {
  onCaptureVistaAmpla: () => void;
  onCaptureServico: () => void;
  onCaptureDetalhe: () => void;
}

export const ActionBar: React.FC<ActionBarProps & { text: string; setText: (s: string) => void }> = ({
  onCaptureVistaAmpla,
  onCaptureServico,
  onCaptureDetalhe,
  text,
  setText
}) => {
  return (
    <div className="fixed bottom-0 left-0 right-0 bg-white/80 backdrop-blur-md border-t border-slate-200 px-4 py-3 flex flex-col gap-3">
      {/* Input de Texto WhatsApp Style */}
      <div className="flex gap-2 items-center">
        <div className="flex-1 bg-slate-100 rounded-full px-4 py-2 flex items-center border border-slate-200 focus-within:border-emerald-500 transition-colors">
          <input 
            type="text" 
            placeholder="Mensagem (Descreva o serviço antes da foto)..." 
            className="flex-1 bg-transparent outline-none text-sm py-1"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </div>
      </div>

      <div className="pb-4 flex justify-around items-center">
        <button 
          onClick={onCaptureVistaAmpla}
          className="flex flex-col items-center gap-1 group"
        >
          <div className="p-3 bg-slate-100 rounded-2xl group-active:scale-95 transition-all text-slate-600">
            <Layout size={20} />
          </div>
          <span className="text-[10px] font-bold text-slate-500 uppercase">Vista Ampla</span>
        </button>

        <button 
          onClick={onCaptureServico}
          className="flex flex-col items-center gap-1 group"
        >
          <div className="p-4 bg-emerald-600 rounded-full shadow-lg shadow-emerald-200 group-active:scale-90 transition-all text-white">
            <PenTool size={24} />
          </div>
          <span className="text-[10px] font-bold text-emerald-600 uppercase">Serviço</span>
        </button>

        <button 
          onClick={onCaptureDetalhe}
          className="flex flex-col items-center gap-1 group"
        >
          <div className="p-3 bg-slate-100 rounded-2xl group-active:scale-95 transition-all text-slate-600">
            <Camera size={20} />
          </div>
          <span className="text-[10px] font-bold text-slate-500 uppercase">Detalhes</span>
        </button>
      </div>
    </div>
  );
};
