@echo off
chcp 65001 >nul
title Gerador de Estrutura de Pastas

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║   🏗️  Gerador de Estrutura de Pastas  v1.1.0                   ║
echo ║   Levantamentos Fotográficos                                  ║
echo ║                                                                ║
echo ║   TM - Sempre Tecnologia                                      ║
echo ║   Thiago Nascimento Barbosa                                    ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

:: Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado! 
    echo    Por favor, instale Python 3.x de https://python.org
    echo.
    pause
    exit /b 1
)

echo ✓ Python encontrado
echo.

:: Verifica e instala dependências
echo 📦 Verificando dependências...
pip show customtkinter >nul 2>&1
if errorlevel 1 (
    echo    Instalando CustomTkinter...
    pip install customtkinter -q
    echo ✓ CustomTkinter instalado
) else (
    echo ✓ CustomTkinter já instalado
)

echo.
echo 🚀 Iniciando aplicação...
echo.

:: Executa a aplicação
python "%~dp0app.py"

if errorlevel 1 (
    echo.
    echo ❌ Erro ao executar a aplicação
    pause
)
