import React from 'react';

interface MessageBubbleProps {
  author: string;
  text: string;
  timestamp: string;
  isMe?: boolean;
  type?: 'text' | 'image';
  photoUrl?: string;
}

export const MessageBubble: React.FC<MessageBubbleProps> = ({ 
  author, 
  text, 
  timestamp, 
  isMe = false,
  type = 'text',
  photoUrl
}) => {
  return (
    <div className={`flex flex-col mb-4 ${isMe ? 'items-end' : 'items-start'}`}>
      <div className={`max-w-[80%] rounded-2xl px-4 py-2 shadow-sm ${
        isMe 
          ? 'bg-emerald-600 text-white rounded-tr-none' 
          : 'bg-white text-slate-900 rounded-tl-none border border-slate-100'
      }`}>
        {!isMe && <p className="text-[10px] font-bold uppercase tracking-wider opacity-60 mb-1">{author}</p>}
        {type === 'image' && photoUrl && (
          <div className="mb-2 overflow-hidden rounded-lg">
            <img src={photoUrl} alt="Captura" className="w-full h-auto object-cover" />
          </div>
        )}
        <p className="text-sm leading-relaxed">{text}</p>
        <p className={`text-[10px] mt-1 text-right ${isMe ? 'text-emerald-100' : 'text-slate-400'}`}>
          {timestamp}
        </p>
      </div>
    </div>
  );
};
