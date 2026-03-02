import os
import shutil
import base64
from io import BytesIO
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image

# Reaproveitar lógica de geração atual
from generator import build_content_from_root, generate_report

app = Flask(__name__)
# Configuração base de CORS para aceitar requisições de localhost:5173 e afins
CORS(app)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(PROJECT_DIR, "templates")
os.makedirs(TEMPLATES_DIR, exist_ok=True)


@app.route("/api/templates", methods=["GET"])
def list_templates():
    try:
        files = [f for f in os.listdir(TEMPLATES_DIR) if f.lower().endswith(".docx")]
        files.sort(key=str.casefold)
        return jsonify({"templates": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/upload-template", methods=["POST"])
def upload_template():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nome de arquivo vazio"}), 400
        
    if file and file.filename.lower().endswith(".docx"):
        filename = secure_filename(file.filename)
        filepath = os.path.join(TEMPLATES_DIR, filename)
        file.save(filepath)
        return jsonify({"message": "Template salvo", "filename": filename})
        
    return jsonify({"error": "Apenas arquivos .docx são permitidos"}), 400


@app.route("/api/scan", methods=["POST"])
def scan_directory():
    data = request.json
    pasta_raiz = data.get("pasta_raiz", "").strip() if data.get("pasta_raiz") else ""
    
    if not pasta_raiz or not os.path.isdir(pasta_raiz):
        return jsonify({"error": "Pasta raiz inválida"}), 400
    
    pasta_saida = data.get("pasta_saida", os.path.join(PROJECT_DIR, "output"))
    os.makedirs(pasta_saida, exist_ok=True)
    log_errors = os.path.join(pasta_saida, "erros_pastas.txt")
    
    def dummy_logger(msg): pass
    
    try:
        conteudo = build_content_from_root(pasta_raiz, log_errors, logger=dummy_logger)
        return jsonify({"conteudo": conteudo})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/thumbnail", methods=["GET"])
def get_thumbnail():
    path = request.args.get("path")
    if not path or not os.path.exists(path):
        return jsonify({"error": "Arquivo não encontrado"}), 404
        
    try:
        img = Image.open(path)
        # Redimensiona mantendo a proporção para caber em 150x150
        img.thumbnail((150, 150), Image.Resampling.LANCZOS)
        
        buffered = BytesIO()
        img_format = img.format if img.format else 'JPEG'
        # Converter para RGB se for PNG caso o format original não defina direito com JPEG
        if img.mode in ('RGBA', 'P') and img_format in ('JPEG', 'JPG'):
             img = img.convert('RGB')
             
        img.save(buffered, format=img_format)
        buffered.seek(0)
        
        return send_file(buffered, mimetype=f"image/{img_format.lower()}")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/generate", methods=["POST"])
def generate_docx():
    data = request.json
    pasta_raiz = data.get("pasta_raiz", "").strip() if data.get("pasta_raiz") else ""
    modelo_nome = data.get("modelo", "").strip() if data.get("modelo") else ""
    pasta_saida = data.get("pasta_saida", "").strip() if data.get("pasta_saida") else ""
    conteudo_editado = data.get("conteudo", [])
    
    if not all([pasta_raiz, modelo_nome, pasta_saida, conteudo_editado]):
        return jsonify({"error": "Faltam parâmetros"}), 400
        
    modelo_path = os.path.join(TEMPLATES_DIR, modelo_nome)
    if not os.path.isfile(modelo_path):
        return jsonify({"error": f"Modelo não encontrado: {modelo_nome}"}), 404
        
    try:
        os.makedirs(pasta_saida, exist_ok=True)
        nome_pasta_raiz = os.path.basename(pasta_raiz.strip(os.sep))
        output_docx = os.path.join(pasta_saida, f"RELATÓRIO FOTOGRÁFICO - {nome_pasta_raiz} - LEVANTAMENTO PREVENTIVO.docx")
        
        log_errors = os.path.join(pasta_saida, "erros_pastas.txt")
        log_process = os.path.join(pasta_saida, "process_log.txt")
        
        def file_logger(msg: str) -> None:
            with open(log_process, "a", encoding="utf-8") as f:
                f.write(msg + "\n")

        with open(log_process, "w", encoding="utf-8") as f:
            f.write("PROCESS LOG - Geração de Relatório via Web\n\n")
            
        file_logger(f"Pasta raiz: {pasta_raiz}")
        file_logger(f"Modelo: {modelo_path}")
        file_logger(f"Saída: {pasta_saida}\n")
        
        total_images = generate_report(modelo_path, conteudo_editado, output_docx, logger=file_logger)
        
        return jsonify({
            "message": "Relatório gerado com sucesso",
            "total_images": total_images,
            "output_docx": output_docx,
            "log_process": log_process,
            "log_errors": log_errors
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/open-folder", methods=["POST"])
def open_folder():
    data = request.json
    path = data.get("path", "").strip() if data.get("path") else ""
    if path and os.path.isdir(path):
        try:
            os.startfile(path)
            return jsonify({"status": "ok"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Pasta inválida"}), 400


import tkinter as tk
from tkinter import filedialog

@app.route("/api/dialog/folder", methods=["GET"])
def ask_directory():
    """Abre o seletor de pastas nativo do Windows e retorna o caminho selecionado"""
    try:
        # Cria uma janela oculta do Tkinter
        root = tk.Tk()
        root.withdraw()
        # Força a janela a ficar no topo para não se perder atrás do navegador
        root.attributes('-topmost', True)
        
        path = filedialog.askdirectory(parent=root, title="Selecione a pasta")
        root.destroy()
        
        return jsonify({"path": path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)

