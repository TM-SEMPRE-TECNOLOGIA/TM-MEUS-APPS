"use client";

import { useState, useEffect, useRef } from 'react';
import {
  FolderOpen,
  FileText,
  Play,
  Eye,
  Terminal,
  CheckCircle2,
  Clock,
  ChevronRight,
  Trash2,
  LayoutGrid,
  Download
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const API_URL = "http://127.0.0.1:5000";

export default function Home() {
  const [pastaRaiz, setPastaRaiz] = useState('');
  const [modeloSelecionado, setModeloSelecionado] = useState('');
  const [pastaSaida, setPastaSaida] = useState('');
  const [tipoRelatorio, setTipoRelatorio] = useState('tradicional');
  const [templates, setTemplates] = useState<string[]>([]);
  const [logs, setLogs] = useState<{ msg: string, type: 'info' | 'success' | 'error' | 'process' }[]>([
    { msg: "🚀 Sistema iniciado. Aguardando configuração...", type: 'process' }
  ]);
  const [conteudo, setConteudo] = useState<any[] | null>(null);
  const [docGerado, setDocGerado] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [mounted, setMounted] = useState(false);

  const logEndRef = useRef<HTMLDivElement>(null);

  const addLog = (msg: string, type: 'info' | 'success' | 'error' | 'process' = 'info') => {
    setLogs(prev => [...prev, { msg, type }]);
  };

  const fetchTemplates = async () => {
    try {
      const res = await fetch(`${API_URL}/api/templates`);
      const data = await res.json();
      if (data.templates) {
        setTemplates(data.templates);
        if (data.templates.length > 0) setModeloSelecionado(data.templates[0]);
      }
    } catch (err) {
      addLog("Erro ao carregar templates. Verifique se o backend Python está rodando.", "error");
    }
  };

  useEffect(() => {
    setMounted(true);
    fetchTemplates();
  }, []);

  useEffect(() => {
    if (mounted) {
      logEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [logs, mounted]);

  if (!mounted) return <div className="min-h-screen" />;

  const selectFolder = async (type: 'raiz' | 'saida') => {
    try {
      const res = await fetch(`${API_URL}/api/dialog/folder`);
      const data = await res.json();
      if (data.path) {
        if (type === 'raiz') {
          setPastaRaiz(data.path);
          addLog(`Pasta raiz selecionada: ${data.path}`, "success");
        } else {
          setPastaSaida(data.path);
          addLog(`Pasta de saída selecionada: ${data.path}`, "success");
        }
      }
    } catch (err) {
      addLog("Erro ao abrir seletor de pastas.", "error");
    }
  };

  const handleScan = async () => {
    if (!pastaRaiz) return addLog("Selecione uma pasta raiz antes de escanear.", "error");

    setLoading(true);
    addLog("Iniciando varredura de pastas...", "process");

    try {
      const res = await fetch(`${API_URL}/api/scan`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pasta_raiz: pastaRaiz, pasta_saida: pastaSaida, tipo_relatorio: tipoRelatorio })
      });
      const data = await res.json();
      if (data.conteudo) {
        setConteudo(data.conteudo);
        addLog(`Varredura concluída. ${data.conteudo.length} elementos encontrados.`, "success");
      } else {
        addLog(data.detail || "Erro inesperado no scan.", "error");
      }
    } catch (err) {
      addLog("Erro na comunicação com o servidor.", "error");
    } finally {
      setLoading(false);
    }
  };

  const handleGenerate = async () => {
    if (!pastaRaiz || !modeloSelecionado || !conteudo) {
      return addLog("Configurações incompletas para geração.", "error");
    }

    setIsGenerating(true);
    addLog("Iniciando geração do documento Word...", "process");

    try {
      const res = await fetch(`${API_URL}/api/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          pasta_raiz: pastaRaiz,
          modelo: modeloSelecionado,
          pasta_saida: pastaSaida || "output",
          conteudo: conteudo,
          tipo_relatorio: tipoRelatorio
        })
      });
      const data = await res.json();
      if (data.message) {
        addLog(`✅ ${data.message}`, "success");
        addLog(`📊 Total de imagens: ${data.total_images}`, "info");
        addLog(`📄 Local: ${data.output_docx}`, "info");
        setDocGerado(data.output_docx);
      } else {
        const errMsg = typeof data.detail === 'string' ? data.detail : JSON.stringify(data.detail);
        addLog(errMsg || "Erro na geração.", "error");
      }
    } catch (err) {
      addLog("Erro crítico na geração.", "error");
    } finally {
      setIsGenerating(false);
    }
  };

  const openFolder = async (path: string) => {
    try {
      await fetch(`${API_URL}/api/open-folder`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ path })
      });
    } catch (err) {
      addLog("Erro ao abrir pasta.", "error");
    }
  };

  const handleDownload = async () => {
    if (!docGerado) return;
    setIsDownloading(true);
    addLog("Iniciando download do relatório...", "process");
    try {
      const res = await fetch(`${API_URL}/api/download?path=${encodeURIComponent(docGerado)}`);
      if (!res.ok) throw new Error(`Erro HTTP ${res.status}`);
      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = docGerado.split('\\').pop() || 'relatorio.docx';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
      addLog("✅ Download concluído!", "success");
    } catch (err) {
      addLog("Erro ao baixar o arquivo.", "error");
    } finally {
      setIsDownloading(false);
    }
  };

  return (
    <div className="flex flex-col min-h-screen">
      <header className="tm-header">
        <div className="tm-logo">
          <div className="tm-logo-mark">TM</div>
          <div className="tm-logo-text">TM <span>Relatório SP</span></div>
        </div>
        <div className="ml-auto flex items-center gap-3">
          <button
            onClick={() => openFolder(pastaSaida || "output")}
            className="tm-btn-secondary flex items-center gap-2"
          >
            <FolderOpen size={16} />
            <span>Abrir Saída</span>
          </button>
          <button
            onClick={handleDownload}
            disabled={!docGerado || isDownloading}
            className={`tm-btn-primary flex items-center gap-2 ${!docGerado ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            {isDownloading ? (
              <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
            ) : (
              <Download size={16} />
            )}
            <span>{isDownloading ? 'Baixando...' : 'Baixar Relatório'}</span>
          </button>
        </div>
      </header>

      <div className="tm-layout">
        <main className="tm-main-content tm-custom-scrollbar">
          <div className="tm-card flex flex-col gap-5">
            <h2 className="text-xl font-bold text-tm-text">Configuração do Relatório</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {/* Step 1: Root Folder */}
              <div className="flex flex-col gap-3">
                <label className="text-sm font-medium text-tm-text-muted">Diretório Raiz</label>
                <div className="tm-input-container">
                  <FolderOpen size={18} className="text-tm-text-subtle" />
                  <input
                    type="text"
                    className="tm-input-field"
                    placeholder="Selecione a pasta com as fotos e subpastas..."
                    value={pastaRaiz}
                    readOnly
                  />
                  <button onClick={() => selectFolder('raiz')} className="tm-btn-secondary p-2">
                    <ChevronRight size={16} />
                  </button>
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={() => setTipoRelatorio('tradicional')}
                    className={`flex-1 tm-btn-secondary py-1.5 px-2 text-xs ${tipoRelatorio === 'tradicional' ? 'bg-[var(--tm-primary-light)] text-[var(--tm-primary)] border-[var(--tm-primary)]' : ''}`}
                  >
                    Tradicional
                  </button>
                  <button
                    onClick={() => setTipoRelatorio('sp')} // Assumindo que 'sp' é o outro tipo de relatório
                    className={`flex-1 tm-btn-secondary py-1.5 px-2 text-xs ${tipoRelatorio === 'sp' ? 'bg-[var(--tm-primary-light)] text-[var(--tm-primary)] border-[var(--tm-primary)]' : ''}`}
                  >
                    SP
                  </button>
                </div>
              </div>

              {/* Step 2: Template Selection */}
              <div className="flex flex-col gap-3">
                <label className="text-sm font-medium text-tm-text-muted">Modelo de Relatório</label>
                <div className="tm-input-container">
                  <FileText size={18} className="text-tm-text-subtle" />
                  <select
                    className="tm-input-field"
                    value={modeloSelecionado}
                    onChange={(e) => setModeloSelecionado(e.target.value)}
                  >
                    {templates.map((template) => (
                      <option key={template} value={template}>
                        {template}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Step 3: Output Folder */}
              <div className="flex flex-col gap-3">
                <label className="text-sm font-medium text-tm-text-muted">Diretório de Saída</label>
                <div className="tm-input-container">
                  <FolderOpen size={18} className="text-tm-text-subtle" />
                  <input
                    type="text"
                    className="tm-input-field"
                    placeholder="Opcional: Selecione a pasta de saída..."
                    value={pastaSaida}
                    readOnly
                  />
                  <button onClick={() => selectFolder('saida')} className="tm-btn-secondary p-2">
                    <ChevronRight size={16} />
                  </button>
                </div>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex gap-4 mt-4">
              <button
                onClick={handleScan}
                disabled={loading || isGenerating}
                className={`tm-btn-primary flex-1 flex items-center justify-center gap-2 ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
              >
                {loading ? (
                  <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                ) : (
                  <Eye size={16} />
                )}
                <span>{loading ? 'Escaneando...' : 'Escanear Pastas'}</span>
              </button>
              <button
                onClick={handleGenerate}
                disabled={!conteudo || isGenerating || loading}
                className={`tm-btn-primary flex-1 flex items-center justify-center gap-2 ${!conteudo || isGenerating || loading ? 'opacity-50 cursor-not-allowed' : ''}`}
              >
                {isGenerating ? (
                  <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                ) : (
                  <Play size={16} />
                )}
                <span>{isGenerating ? 'Gerando...' : 'Gerar Relatório'}</span>
              </button>
            </div>
          </div>

          {/* Log Console */}
          <div className="tm-card flex flex-col gap-4 flex-1">
            <h2 className="text-xl font-bold text-tm-text">Console de Logs</h2>
            <div className="flex-1 bg-[var(--tm-bg-input)] rounded-lg p-4 overflow-y-auto tm-custom-scrollbar">
              <AnimatePresence>
                {logs.map((log, i) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    transition={{ duration: 0.2 }}
                    className={`tm-log-item ${log.type}`}
                  >
                    <span className="tm-log-icon">
                      {log.type === 'info' && <Terminal size={16} />}
                      {log.type === 'success' && <CheckCircle2 size={16} />}
                      {log.type === 'error' && <Trash2 size={16} />}
                      {log.type === 'process' && <Clock size={16} />}
                    </span>
                    <span className="tm-log-message">[{new Date().toLocaleTimeString('pt-BR', { hour12: false })}] {log.msg}</span>
                  </motion.div>
                ))}
              </AnimatePresence>
              <div ref={logEndRef} />
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}
