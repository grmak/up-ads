import os
import sys
import subprocess
from typing import List

PASTA_LAB = "laboratorio"

def listar_aulas() -> List[str]:
    """
    Lista todos os arquivos de aula disponíveis na pasta PASTA_LAB.
    
    A função varre o diretório especificado por PASTA_LAB e retorna
    uma lista ordenada com nomes de arquivos que começam com "aula"
    e terminam com ".py".
    
    Returns:
        List[str]: Lista ordenada de nomes de arquivos de aula.
        
    Example:
        >>> PASTA_LAB = "./exemplos"
        >>> listar_aulas()
        ['aula1.py', 'aula2.py', 'aula3.py']
        
    Note:
        Assume que PASTA_LAB está definida globalmente e contém
        apenas arquivos .py válidos.
    """    
    arquivos = []
    
    for nome in os.listdir(PASTA_LAB):
        if nome.startswith("aula") and nome.endswith(".py"):
            arquivos.append(nome)
    
    arquivos.sort()
    return arquivos


def exibir_menu(arquivos: List[str]) -> None:
    """
    Exibe um menu interativo com as aulas disponíveis.
    
    Apresenta uma lista numerada das aulas encontradas, permitindo
    que o usuário selecione qual executar. O menu mostra também
    a opção 0 para sair.
    
    Args:
        arquivos (List[str]): Lista de nomes dos arquivos de aula.
        
    Example:
        >>> arquivos = ['aula1.py', 'aula2.py']
        >>> exibir_menu(arquivos)
        
        === MENU DE AULAS ===
        1 - Executar aula1.py
        2 - Executar aula2.py
        0 - Sair
        
    Note:
        A numeração começa em 1 e corresponde à posição na lista.
    """    
    print("\n=== MENU DE AULAS ===")
    
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i:02d} - Executar {arquivo}")
    
    print("00 - Sair")


def executar_arquivo(nome_arquivo: str) -> None:
    """
    Executa um arquivo Python específico usando subprocess.
    
    Constrói o caminho completo para o arquivo dentro de PASTA_LAB
    e o executa como um processo filho usando o interpretador Python.
    
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
    1. Lista as aulas disponíveis
    2. Exibe o menu interativo
    3. Processa a escolha do usuário
    4. Executa a aula selecionada
    5. Retorna ao menu até que o usuário saia
    
    Example:
        >>> if __name__ == "__main__":
        ...     main()
        
    Note:
        A função continua em execução até que o usuário escolha
        a opção 0 (Sair) no menu.
    """    
    while True:
        arquivos = listar_aulas()
        
        if not arquivos:
            print("Nenhum arquivo aula*.py encontrado.")
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
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()