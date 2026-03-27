'use client';

import { useState } from 'react';
import { SetupFlow } from '@/components/chat/SetupFlow';
import { ChatLayout } from '@/components/chat/ChatLayout';

export default function OSPage() {
  const [view, setView] = useState<'setup' | 'chat'>('setup');
  const [sessionInfo, setSessionInfo] = useState({ area: '', environment: '' });

  const handleSetupComplete = (area: string, environment: string) => {
    setSessionInfo({ area, environment });
    setView('chat');
  };

  return (
    <main className="min-h-screen">
      {view === 'setup' ? (
        <SetupFlow onComplete={handleSetupComplete} />
      ) : (
        <ChatLayout 
          orderId="OS-2024-001"
          clientName="Sempre Tecnologia"
          projectName={sessionInfo.environment}
          area={sessionInfo.area}
          env={sessionInfo.environment}
          onBack={() => setView('setup')}
        />
      )}
    </main>
  );
}
