import os
import sys

# Configurações
BACKEND_SP = r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\NX Relatorios SP\APP\backend"
DATA_RAIZ = r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\TM Relatorio Final\ITAMONTE - (Relatório sendo feito)"
TEMPLATE_PADRAO = r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\NX Relatorios SP\APP\backend\templates\MODELO - 0908 - SAO PAULO - ATUALIZADO.docx"
OUTPUT_DIR = r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\TESTES_COMPARATIVOS"

# Setup Path
if BACKEND_SP not in sys.path:
    sys.path.insert(0, BACKEND_SP)

try:
    import generator_sp
    print(">>> Iniciando Geração SP Expert...")
    result = generator_sp.run_all_sp(DATA_RAIZ, TEMPLATE_PADRAO, OUTPUT_DIR)
    print(f"✅ Sucesso! Relatório SP gerado em: {result.output_docx}")
    print(f"Total de imagens: {result.total_images}")
except Exception as e:
    print(f"❌ Erro na Geração SP: {e}")
    import traceback
    traceback.print_exc()
