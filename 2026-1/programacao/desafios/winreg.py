import tkinter as tk
from tkinter import ttk, messagebox
import winreg
import threading

class PesquisaProgramasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pesquisa de Programas Instalados")
        self.root.geometry("800x600")
        
        self.programas = []
        
        # Frame de pesquisa
        frame_pesquisa = tk.Frame(root)
        frame_pesquisa.pack(pady=10, padx=10, fill=tk.X)
        
        tk.Label(frame_pesquisa, text="Pesquisar:").pack(side=tk.LEFT, padx=5)
        self.entry_pesquisa = tk.Entry(frame_pesquisa)
        self.entry_pesquisa.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.entry_pesquisa.bind('<KeyRelease>', self.pesquisar)
        
        # Opções de pesquisa
        self.opcao_pesquisa = tk.StringVar(value="ambos")
        frame_opcoes = tk.Frame(root)
        frame_opcoes.pack(pady=5)
        
        tk.Radiobutton(frame_opcoes, text="Nome e Descrição", variable=self.opcao_pesquisa, 
                      value="ambos", command=self.pesquisar).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_opcoes, text="Apenas Nome", variable=self.opcao_pesquisa, 
                      value="nome", command=self.pesquisar).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_opcoes, text="Apenas Descrição", variable=self.opcao_pesquisa, 
                      value="descricao", command=self.pesquisar).pack(side=tk.LEFT, padx=10)
        
        # Treeview para mostrar resultados
        frame_tree = tk.Frame(root)
        frame_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar_y = tk.Scrollbar(frame_tree)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scrollbar_x = tk.Scrollbar(frame_tree, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree = ttk.Treeview(frame_tree, columns=('nome', 'descricao', 'fabricante', 'versao'),
                                 yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        self.tree.heading('#0', text='#')
        self.tree.heading('nome', text='Nome do Programa')
        self.tree.heading('descricao', text='Descrição')
        self.tree.heading('fabricante', text='Fabricante')
        self.tree.heading('versao', text='Versão')
        
        self.tree.column('#0', width=50)
        self.tree.column('nome', width=250)
        self.tree.column('descricao', width=300)
        self.tree.column('fabricante', width=150)
        self.tree.column('versao', width=100)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        # Status
        self.status = tk.Label(root, text="Carregando programas...", fg="blue")
        self.status.pack(pady=5)
        
        # Botão atualizar
        btn_atualizar = tk.Button(root, text="Atualizar Lista", command=self.carregar_programas)
        btn_atualizar.pack(pady=5)
        
        # Carrega os programas
        self.carregar_programas()
    
    def carregar_programas(self):
        """Carrega programas em thread separada"""
        self.status.config(text="Carregando lista de programas...", fg="blue")
        thread = threading.Thread(target=self._carregar_programas_thread)
        thread.start()
    
    def _carregar_programas_thread(self):
        """Carrega programas do registro"""
        programas = []
        caminhos = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]
        
        for caminho in caminhos:
            try:
                chave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, caminho, 0, winreg.KEY_READ)
                for i in range(winreg.QueryInfoKey(chave)[0]):
                    try:
                        subchave_nome = winreg.EnumKey(chave, i)
                        subchave = winreg.OpenKey(chave, subchave_nome)
                        
                        nome = None
                        descricao = None
                        fabricante = None
                        versao = None
                        
                        try:
                            nome = winreg.QueryValueEx(subchave, "DisplayName")[0]
                        except:
                            pass
                        
                        try:
                            descricao = winreg.QueryValueEx(subchave, "Comments")[0]
                        except:
                            pass
                        
                        try:
                            fabricante = winreg.QueryValueEx(subchave, "Publisher")[0]
                        except:
                            pass
                        
                        try:
                            versao = winreg.QueryValueEx(subchave, "DisplayVersion")[0]
                        except:
                            pass
                        
                        if nome:
                            programas.append({
                                'nome': nome,
                                'descricao': descricao if descricao else '',
                                'fabricante': fabricante if fabricante else '',
                                'versao': versao if versao else ''
                            })
                        
                        winreg.CloseKey(subchave)
                    except:
                        pass
                winreg.CloseKey(chave)
            except:
                pass
        
        # Remove duplicatas
        programas_unicos = []
        vistos = set()
        for p in programas:
            if p['nome'] not in vistos:
                vistos.add(p['nome'])
                programas_unicos.append(p)
        
        self.programas = sorted(programas_unicos, key=lambda x: x['nome'].lower())
        
        # Atualiza interface
        self.root.after(0, self._atualizar_lista)
    
    def _atualizar_lista(self):
        """Atualiza a lista na interface"""
        self.pesquisar()
        self.status.config(text=f"Total: {len(self.programas)} programas carregados", fg="green")
    
    def pesquisar(self, event=None):
        """Pesquisa programas baseado no termo e opção"""
        # Limpa a treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        termo = self.entry_pesquisa.get().strip().lower()
        opcao = self.opcao_pesquisa.get()
        
        resultados = []
        if not termo:
            resultados = self.programas
        else:
            for prog in self.programas:
                if opcao == 'nome':
                    if termo in prog['nome'].lower():
                        resultados.append(prog)
                elif opcao == 'descricao':
                    if termo in prog['descricao'].lower():
                        resultados.append(prog)
                else:  # ambos
                    if termo in prog['nome'].lower() or termo in prog['descricao'].lower():
                        resultados.append(prog)
        
        # Insere resultados na treeview
        for i, prog in enumerate(resultados, 1):
            self.tree.insert('', 'end', text=str(i),
                           values=(prog['nome'], prog['descricao'][:100] + '...' if len(prog['descricao']) > 100 else prog['descricao'],
                                  prog['fabricante'], prog['versao']))
        
        self.status.config(text=f"Resultados: {len(resultados)} de {len(self.programas)} programas")

# Executar
if __name__ == "__main__":
    root = tk.Tk()
    app = PesquisaProgramasGUI(root)
    root.mainloop()