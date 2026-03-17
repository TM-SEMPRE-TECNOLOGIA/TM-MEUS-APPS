import os
import sys
import re

# Adicionar backend ao path para importar word_utils
backend_path = os.path.abspath(r"C:\Users\thiag\TM-MEUS-APPS\0 - NEXT APPS\TM Relatorio SP\APP\backend")
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from word_utils import inserir_conteudo

ORDEM_PASTAS = ["- Área externa", "- Área interna", "- Segundo piso"]

def folder_sort_key(name: str):
    name_lower = name.lower()
    if "vista ampla" in name_lower:
        return (0, name_lower)
    
    match = re.match(r'^(\d+)(.*)', name)
    if match:
        return (1, int(match.group(1)), match.group(2))
        
    if "detalhes" in name_lower:
        return (3, name_lower)
        
    return (2, name_lower)

def build_content_perfect(pasta_raiz: str) -> list:
    conteudo = []
    
    for root_dir, dirs, files in os.walk(pasta_raiz, topdown=True):
        try:
            root_dir = os.fsdecode(root_dir)
            dirs[:] = [os.fsdecode(d) for d in dirs]
            files = [os.fsdecode(f) for f in files]
        except Exception as e:
            continue

        if root_dir == pasta_raiz:
            dirs.sort(
                key=lambda x: (
                    0 if x == "- Vista ampla" else 1,
                    ORDEM_PASTAS.index(x) if x in ORDEM_PASTAS else len(ORDEM_PASTAS),
                    folder_sort_key(x),
                )
            )
        else:
            dirs.sort(key=folder_sort_key)

        path_parts = os.path.relpath(root_dir, pasta_raiz).split(os.sep)
        nome = path_parts[-1]

        if nome != ".":
            nivel = len(path_parts)
            prefixos = {1: "", 2: "»", 3: "»»"}
            conteudo.append(f"{prefixos.get(nivel, '»»»')}{nome}")

        try:
            arquivos_imagens = [
                os.path.join(root_dir, f)
                for f in files
                if f.lower().endswith((".png", ".jpg", ".jpeg"))
            ]
            try:
                arquivos_imagens.sort(key=os.path.getctime)
            except Exception:
                arquivos_imagens.sort()

            for imagem_path in arquivos_imagens:
                if os.path.exists(imagem_path):
                    conteudo.append({"imagem": imagem_path})

            # Sempre adiciona quebra de página ao final do bloco (se houver imagens ou o diretório)
            conteudo.append({"quebra_pagina": True})

        except Exception as e_dir:
            continue

    return conteudo


if __name__ == "__main__":
    pasta_raiz = r"C:\Users\thiag\TM-MEUS-APPS\0 - NEXT APPS\TM Relatorio Final\ITAMONTE - (Relatório sendo feito)"
    modelo_path = os.path.join(backend_path, "templates", "MODELO - 0908 - SAO PAULO.docx")

    pasta_saida = r"C:\Users\thiag\TM-MEUS-APPS\0 - NEXT APPS\TM Relatorio Final"
    
    os.makedirs(pasta_saida, exist_ok=True)
    nome_pasta_raiz = os.path.basename(pasta_raiz.strip(os.sep))
    output_docx_path = os.path.join(pasta_saida, f"RELATÓRIO FOTOGRÁFICO - {nome_pasta_raiz} - NOVAORDEM.docx")
    
    print(f"Lendo estrutura da pasta: {pasta_raiz}")
    conteudo = build_content_perfect(pasta_raiz)
    
    print("Conteúdo gerado será inserido no modelo docx...")
    total = inserir_conteudo(modelo_path, conteudo, output_docx_path)
    
    print(f"Sucesso! Relatório salvo em: {output_docx_path}")
    print(f"Total de imagens inseridas: {total}")
