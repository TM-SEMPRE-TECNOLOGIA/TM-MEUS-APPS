import os
import sys
import shutil
import importlib.util

# Configurações
DATA_RAIZ = r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\TM Relatorio Final\ITAMONTE - (Relatório sendo feito)"
TEMPLATE_PADRAO = r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\NX Relatorios SP\APP\backend\templates\MODELO - 0908 - SAO PAULO - ATUALIZADO.docx"
OUTPUT_DIR = r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\TESTES_COMPARATIVOS"

OS_APPS = {
    "TM_Relatorio_Base": r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\TM Relatorio",
    "NX_Relatorios_SP_Perfeito": r"C:\Users\thiag\TM-MEUS-APPS\.NEXT APPS\NX Relatorios SP\APP\backend"
}

os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_test_for_app(app_name, backend_path):
    print(f"\n>>> Testando App: {app_name}")
    
    # Limpa sys.modules para evitar conflito de importação
    if 'generator' in sys.modules: del sys.modules['generator']
    if 'word_utils' in sys.modules: del sys.modules['word_utils']
    
    # Adiciona ao path
    if backend_path not in sys.path:
        sys.path.insert(0, backend_path)
    
    try:
        import generator
        import word_utils
        
        output_file = os.path.join(OUTPUT_DIR, f"TESTE_{app_name}.docx")
        log_errors = os.path.join(OUTPUT_DIR, f"erros_{app_name}.txt")
        
        print(f"Lendo conteúdo...")
        conteudo = generator.build_content_from_root(DATA_RAIZ, log_errors)
        
        print(f"Gerando DOCX...")
        # Verifica se o inserir_conteudo aceita selected_description (Versão SP aceita)
        import inspect
        sig = inspect.signature(word_utils.inserir_conteudo)
        
        if 'selected_description' in sig.parameters:
            total = word_utils.inserir_conteudo(TEMPLATE_PADRAO, conteudo, output_file, selected_description="TESTE COMPARATIVO EXECUTIVO")
        else:
            total = word_utils.inserir_conteudo(TEMPLATE_PADRAO, conteudo, output_file)
            
        print(f"Sucesso! {total} imagens inseridas em {output_file}")
        return True
    except Exception as e:
        print(f"Erro ao testar {app_name}: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if backend_path in sys.path:
            sys.path.remove(backend_path)

if __name__ == "__main__":
    results = {}
    for name, path in OS_APPS.items():
        results[name] = run_test_for_app(name, path)
    
    print("\n\n=== RESUMO DOS TESTES ===")
    for name, success in results.items():
        status = "✅ OK" if success else "❌ FALHA"
        print(f"{name}: {status}")
