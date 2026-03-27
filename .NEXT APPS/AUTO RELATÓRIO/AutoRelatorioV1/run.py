"""
TM · Sempre Tecnologia — Launcher Premium
Gerencia backend (FastAPI) e frontend (Next.js) em um único terminal.
"""

import os
import sys
import signal
import subprocess
import threading
import time
import datetime
import urllib.request
import urllib.error

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich.table import Table
from rich import box

# ─── Configurações ──────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "APP", "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "APP", "frontend")
LOG_DIR = os.path.join(BASE_DIR, "logs")
BACKEND_URL = "http://127.0.0.1:5000/docs"
FRONTEND_URL = "http://localhost:3000"
HEALTH_TIMEOUT = 30  # segundos máximo para o backend responder
VENV_PYTHON = os.path.join(BACKEND_DIR, ".venv", "Scripts", "python.exe")

os.makedirs(LOG_DIR, exist_ok=True)

# ─── Console Rich ───────────────────────────────────────────────
console = Console()
processes: list[subprocess.Popen] = []


def get_python():
    """Retorna o caminho do Python do .venv se existir, senão usa o do sistema."""
    if os.path.isfile(VENV_PYTHON):
        return VENV_PYTHON
    return sys.executable


def show_banner():
    """Exibe o banner profissional do sistema."""
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    title = Text()
    title.append("TM", style="bold bright_white")
    title.append(" · ", style="dim white")
    title.append("SEMPRE TECNOLOGIA", style="bold cyan")

    subtitle = Text()
    subtitle.append("Gerador de Relatório", style="dim white")
    subtitle.append("  ·  ", style="dim")
    subtitle.append(f"v1.0", style="dim bright_cyan")
    subtitle.append("  ·  ", style="dim")
    subtitle.append(now, style="dim white")

    content = Text.assemble(title, "\n", subtitle)

    panel = Panel(
        content,
        border_style="bright_cyan",
        box=box.ROUNDED,
        padding=(1, 3),
    )
    console.print()
    console.print(panel)
    console.print()


def stream_output(process: subprocess.Popen, label: str, color: str, log_file: str):
    """Lê stdout do processo e imprime com prefixo colorido + salva em log."""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Sessão iniciada em {datetime.datetime.now().isoformat()}\n")
        f.write(f"{'='*60}\n\n")

        for line in iter(process.stdout.readline, ""):
            if not line:
                break
            line = line.rstrip()
            if not line:
                continue

            # Salvar no arquivo de log
            f.write(f"{line}\n")
            f.flush()

            # Determinar estilo baseado no conteúdo
            style = "dim white"
            prefix_style = f"bold {color}"

            line_lower = line.lower()
            if any(kw in line_lower for kw in ["error", "erro", "exception", "traceback", "failed"]):
                style = "bold red"
            elif any(kw in line_lower for kw in ["warning", "warn", "aviso"]):
                style = "yellow"
            elif any(kw in line_lower for kw in ["ready", "started", "running", "pronto", "✓", "compiled"]):
                style = "green"

            # Printar com prefixo
            output = Text()
            output.append(f"  [{label}] ", style=prefix_style)
            output.append(line, style=style)
            console.print(output)

    # Se saiu do loop, o processo morreu
    exit_code = process.poll()
    if exit_code is not None and exit_code != 0:
        console.print()
        console.print(
            Panel(
                f"[bold red]❌ {label} encerrou com código {exit_code}[/]\n"
                f"[dim]Verifique os logs em: logs/{label.lower()}.log[/]",
                border_style="red",
                box=box.ROUNDED,
            )
        )


def start_process(cmd: list, cwd: str, label: str, color: str, log_name: str) -> subprocess.Popen:
    """Inicia um subprocesso com stdout/stderr capturados."""
    log_file = os.path.join(LOG_DIR, log_name)

    env = os.environ.copy()
    # Forçar saída sem buffer para o Python
    env["PYTHONUNBUFFERED"] = "1"
    # Forçar cores ANSI no Next.js
    env["FORCE_COLOR"] = "1"

    proc = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
    )
    processes.append(proc)

    # Thread para ler o output em background
    thread = threading.Thread(
        target=stream_output,
        args=(proc, label, color, log_file),
        daemon=True,
    )
    thread.start()

    return proc


def wait_for_backend():
    """Aguarda o backend responder com spinner animado."""
    start_time = time.time()

    with Live(
        Spinner("dots", text="[bright_cyan]  Aguardando Backend responder...[/]", style="bright_cyan"),
        console=console,
        refresh_per_second=10,
        transient=True,
    ):
        while time.time() - start_time < HEALTH_TIMEOUT:
            try:
                req = urllib.request.urlopen(BACKEND_URL, timeout=2)
                if req.status == 200:
                    return True
            except (urllib.error.URLError, ConnectionRefusedError, OSError):
                pass
            time.sleep(0.5)

    return False


def show_ready():
    """Exibe o painel de 'sistema pronto'."""
    content = Text()
    content.append("  🟢  SISTEMA PRONTO\n\n", style="bold bright_green")
    content.append("  🌐  ", style="")
    content.append(FRONTEND_URL, style="bold underline bright_cyan")
    content.append("\n  📋  ", style="")
    content.append(f"{BACKEND_URL.replace('/docs', '')} (API)", style="dim white")
    content.append("\n\n  ⌨   ", style="")
    content.append("Ctrl+C", style="bold bright_white")
    content.append(" para encerrar tudo", style="dim white")

    console.print()
    console.print(Panel(content, border_style="green", box=box.ROUNDED, padding=(0, 1)))
    console.print()
    console.print("  [dim]─── Logs em tempo real ───[/]")
    console.print()


def shutdown(signum=None, frame=None):
    """Encerra todos os subprocessos de forma limpa."""
    console.print()
    console.print("  [dim yellow]⏳ Encerrando processos...[/]")

    for proc in processes:
        try:
            if os.name == "nt":
                proc.terminate()
            else:
                proc.send_signal(signal.SIGTERM)
        except (OSError, ProcessLookupError):
            pass

    # Aguardar encerramento
    for proc in processes:
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()

    console.print("  [bold green]✅ Tudo encerrado. Até a próxima![/]")
    console.print()
    sys.exit(0)


def main():
    # Registrar handler de Ctrl+C
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    # Limpar tela
    os.system("cls" if os.name == "nt" else "clear")

    # Banner
    show_banner()

    # ─── PASSO 1: Backend ───────────────────────────────────────
    python_path = get_python()
    console.print("  [bold bright_cyan]⚡[/] [white]Iniciando Backend FastAPI...[/]")

    backend_proc = start_process(
        cmd=[python_path, "server.py"],
        cwd=BACKEND_DIR,
        label="Backend",
        color="bright_magenta",
        log_name="backend.log",
    )

    # Health-check com spinner
    backend_ok = wait_for_backend()

    if not backend_ok:
        console.print("  [bold red]❌ Backend não respondeu em {HEALTH_TIMEOUT}s[/]")
        console.print("  [dim]Verifique os logs em: logs/backend.log[/]")
        shutdown()
        return

    console.print("  [bold green]✅[/] [white]Backend rodando na porta 5000[/]")
    console.print()

    # ─── PASSO 2: Frontend ──────────────────────────────────────
    console.print("  [bold bright_cyan]⚡[/] [white]Iniciando Frontend Next.js...[/]")

    frontend_proc = start_process(
        cmd=["npm", "run", "dev"],
        cwd=FRONTEND_DIR,
        label="Frontend",
        color="bright_blue",
        log_name="frontend.log",
    )

    # Aguardar um pouco para o frontend compilar
    time.sleep(3)
    console.print("  [bold green]✅[/] [white]Frontend iniciado[/]")

    # ─── PRONTO ─────────────────────────────────────────────────
    show_ready()

    # Manter vivo e monitorar processos
    try:
        while True:
            # Verificar se algum processo morreu
            if backend_proc.poll() is not None:
                console.print("\n  [bold red]⚠  Backend caiu! Verificando logs...[/]")
                break
            if frontend_proc.poll() is not None:
                console.print("\n  [bold red]⚠  Frontend caiu! Verificando logs...[/]")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        pass

    shutdown()


if __name__ == "__main__":
    main()
