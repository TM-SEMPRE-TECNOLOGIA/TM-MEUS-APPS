import React, { useState } from 'react';
import { ChevronLeft, Info, MoreVertical, Phone, Video } from 'lucide-react';
import { MessageBubble } from './MessageBubble';
import { ActionBar } from './ActionBar';
import { saveCapture } from '@/lib/os-actions';

interface ChatLayoutProps {
  orderId: string;
  clientName: string;
  projectName: string;
  area: string;
  env: string;
  onBack: () => void;
}

export const ChatLayout: React.FC<ChatLayoutProps & { area: string; env: string }> = ({
  orderId,
  clientName,
  projectName,
  area,
  env,
  onBack
}) => {
  const [text, setText] = useState('');
  const [messages, setMessages] = useState<any[]>([
    { id: '1', author: 'Sistema', text: `Ordem de Serviço #${orderId} iniciada. Área: ${area}`, timestamp: '10:00', isMe: false, type: 'text' },
    { id: '2', author: 'Thiago (Gestor)', text: `Iniciando vistorias em ${env}.`, timestamp: '10:02', isMe: false, type: 'text' },
  ]);

  const handleCapture = async (type: string) => {
    // Para teste: criando um mock de arquivo
    const blob = new Blob(['mock content'], { type: 'image/jpeg' });
    const file = new File([blob], 'captura.jpg', { type: 'image/jpeg' });

    const formData = new FormData();
    formData.append('orderId', orderId);
    formData.append('clientName', clientName);
    formData.append('area', area);
    formData.append('environment', env);
    formData.append('type', type);
    formData.append('description', text);
    formData.append('file', file);

    try {
      const result = await saveCapture(formData);
      if (result.success) {
        const newMsg = {
          id: result.item.id,
          author: 'Técnico',
          text: text || `${type} realizada.`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          isMe: true,
          type: 'image' as const,
          photoUrl: 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80&w=400'
        };
        setMessages([...messages, newMsg]);
        setText('');
      }
    } catch (err) {
      console.error('Erro ao capturar:', err);
      alert('Erro ao salvar captura. Verifique o console.');
    }
  };

  return (
    <div className="flex flex-col h-screen bg-[#F0F2F5] font-sans">
      {/* Header Estilo WhatsApp */}
      <header className="bg-emerald-600 text-white px-4 py-3 flex items-center gap-3 shadow-md z-10">
        <button onClick={onBack} className="p-1 -ml-1">
          <ChevronLeft size={24} />
        </button>
        <div className="w-10 h-10 rounded-full bg-emerald-500 border border-emerald-400 flex items-center justify-center font-bold text-lg shadow-inner">
          {clientName.charAt(0)}
        </div>
        <div className="flex-1 min-w-0">
          <h1 className="font-bold text-base truncate">{clientName}</h1>
          <h2 className="text-[10px] opacity-80 uppercase tracking-widest">{projectName} • Online</h2>
        </div>
        <div className="flex gap-4 opacity-90">
          <Video size={20} />
          <Phone size={20} />
          <MoreVertical size={20} />
        </div>
      </header>

      {/* Chat Area */}
      <main className="flex-1 overflow-y-auto p-4 pb-48 custom-scrollbar space-y-2">
        <div className="flex justify-center my-4">
          <span className="bg-white/60 backdrop-blur-sm px-3 py-1 rounded-lg text-[10px] uppercase font-bold text-slate-500 shadow-sm border border-slate-100">
            Hoje
          </span>
        </div>
        
        {messages.map((msg) => (
          <MessageBubble 
            key={msg.id}
            author={msg.author}
            text={msg.text}
            timestamp={msg.timestamp}
            isMe={msg.isMe}
            type={msg.type}
            photoUrl={msg.photoUrl}
          />
        ))}
      </main>

      {/* Action Bar */}
      <ActionBar 
        onCaptureVistaAmpla={() => handleCapture('VISTA_AMPLA')}
        onCaptureServico={() => handleCapture('SERVICO')}
        onCaptureDetalhe={() => handleCapture('DETALHE')}
        text={text}
        setText={setText}
      />
    </div>
  );
};
