import os
import sys
import subprocess
from typing import List

# Pasta atual
PASTA_LAB = "./"

def listar_programas() -> List[str]:
    """
    Lista todos os arquivos python disponíveis na pasta PASTA_LAB.
    
    Returns:
        List[str]: Lista ordenada de nomes de arquivos.        
    """    
    arquivos = []
    
    for nome in os.listdir(PASTA_LAB):
        if nome.endswith(".py") and (nome != "menu.py"):
           arquivos.append(nome)
    
    arquivos.sort()
    return arquivos


def exibir_menu(arquivos: List[str]) -> None:
    """
    Exibe um menu interativo com as programas disponíveis.
    
    Args:
        arquivos (List[str]): Lista de nomes dos arquivos python.
        
        === MENU DE EXECUÇÕES ===
        1 - Executar programa1.py
        2 - Executar programa2.py
        0 - Sair
        
    Note:
        A numeração começa em 1 e corresponde à posição na lista.
    """    
    print("\n=== MENU DE PROGRAMAS ===")
    
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i:02d} - Executar {arquivo}")
    
    print("00 - Sair")


def executar_arquivo(nome_arquivo: str) -> None:
    """
    Executa um arquivo Python específico usando subprocess (processo filho).
    
    Args:
        nome_arquivo (str): Nome do arquivo .py a ser executado.
    """
    arq = os.path.join(PASTA_LAB, nome_arquivo)  
    
    print("\nExecutando > ", arq)
    
    subprocess.run([sys.executable, arq])


def main() -> None:
    """
    Função principal do gerenciador de aulas.
    
    Gerencia o loop principal do programa, que:
    1. Listar os programas python disponiveis na pasta
    2. Exibe o menu interativo
    3. Processa a escolha do usuário
    4. Executa o programa selecionado
    5. Retorna ao menu até que o usuário saia
    
    Example:
        >>> if __name__ == "__main__":
        ...     main()
        
    Note:
        A função continua em execução até que o usuário escolha
        a opção 0 (Sair) no menu.
    """    
    while True:
        arquivos = listar_programas()
        
        if not arquivos:
            print("Nenhum arquivo *.py encontrado.")
            break
        
        exibir_menu(arquivos)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            subprocess.run(["clear"])
            continue
        
        if opcao == 0:
            print("Saindo...")
            break
        
        if 1 <= opcao <= len(arquivos):
            executar_arquivo(arquivos[opcao - 1])
            input("\nDigite alguma tecla para carregar o MENU ...")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()