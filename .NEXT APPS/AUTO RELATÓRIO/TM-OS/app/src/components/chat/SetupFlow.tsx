import React, { useState } from 'react';
import { MapPin, Home, ArrowRight, Settings } from 'lucide-react';

interface SetupFlowProps {
  onComplete: (area: string, environment: string) => void;
}

export const SetupFlow: React.FC<SetupFlowProps> = ({ onComplete }) => {
  const [step, setStep] = useState(1);
  const [area, setArea] = useState('');
  const [environment, setEnvironment] = useState('');

  const areas = ['- Área externa', '- Área interna', '- Segundo piso'];
  const environments: Record<string, string[]> = {
    '- Área externa': ['Jardim', 'Piscina', 'Fachada', 'Estacionamento'],
    '- Área interna': ['Sala', 'Cozinha', 'Quarto 01', 'Banheiro'],
    '- Segundo piso': ['Sotão', 'Suíte Master', 'Escritório']
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col p-6 animate-in fade-in duration-500">
      <div className="mt-12 mb-8">
        <div className="w-12 h-1 bg-emerald-600 rounded-full mb-4"></div>
        <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight">
          {step === 1 ? 'Onde você está trabalhando?' : 'Qual o ambiente específico?'}
        </h1>
        <p className="text-slate-500 mt-2 font-medium">
          {step === 1 ? 'Selecione a área principal da vistoria.' : `Área selecionada: ${area}`}
        </p>
      </div>

      <div className="flex-1 space-y-3">
        {step === 1 ? (
          areas.map((a) => (
            <button
              key={a}
              onClick={() => { setArea(a); setStep(2); }}
              className="w-full bg-white p-5 rounded-2xl border border-slate-200 flex items-center justify-between group active:scale-[0.98] transition-all shadow-sm hover:border-emerald-200 hover:shadow-md"
            >
              <div className="flex items-center gap-4">
                <div className="p-3 bg-emerald-50 rounded-xl text-emerald-600 group-hover:bg-emerald-600 group-hover:text-white transition-colors">
                  <MapPin size={24} />
                </div>
                <span className="font-bold text-slate-700">{a}</span>
              </div>
              <ArrowRight size={20} className="text-slate-300" />
            </button>
          ))
        ) : (
          environments[area]?.map((e) => (
            <button
              key={e}
              onClick={() => onComplete(area, e)}
              className="w-full bg-white p-5 rounded-2xl border border-slate-200 flex items-center justify-between group active:scale-[0.98] transition-all shadow-sm hover:border-emerald-200 hover:shadow-md"
            >
              <div className="flex items-center gap-4">
                <div className="p-3 bg-slate-50 rounded-xl text-slate-400 group-hover:bg-emerald-600 group-hover:text-white transition-colors">
                  <Home size={24} />
                </div>
                <span className="font-bold text-slate-700">{e}</span>
              </div>
              <ArrowRight size={20} className="text-slate-300" />
            </button>
          ))
        )}
      </div>

      <div className="py-8 flex justify-between items-center text-[10px] font-bold text-slate-400 uppercase tracking-widest">
        <span>TM Sempre Tecnologia</span>
        <span>Passo {step} de 2</span>
      </div>
    </div>
  );
};
