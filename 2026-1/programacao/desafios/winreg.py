import tkinter as tk
from tkinter import ttk, messagebox
import winreg
import threading
import subprocess
import os

class PesquisaProgramasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pesquisa de Programas Instalados - Versão Completa")
        self.root.geometry("1000x700")
        
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
        
        # Frame para Treeview e botões
        frame_principal = tk.Frame(root)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview com scrollbars
        frame_tree = tk.Frame(frame_principal)
        frame_tree.pack(fill=tk.BOTH, expand=True)
        
        scrollbar_y = tk.Scrollbar(frame_tree)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scrollbar_x = tk.Scrollbar(frame_tree, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree = ttk.Treeview(frame_tree, columns=('nome', 'descricao', 'executavel', 'fabricante', 'versao', 'fonte'),
                                 yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        self.tree.heading('#0', text='#')
        self.tree.heading('nome', text='Nome do Programa')
        self.tree.heading('descricao', text='Descrição')
        self.tree.heading('executavel', text='Executável')
        self.tree.heading('fabricante', text='Fabricante')
        self.tree.heading('versao', text='Versão')
        self.tree.heading('fonte', text='Fonte')
        
        self.tree.column('#0', width=50)
        self.tree.column('nome', width=250)
        self.tree.column('descricao', width=300)
        self.tree.column('executavel', width=200)
        self.tree.column('fabricante', width=150)
        self.tree.column('versao', width=100)
        self.tree.column('fonte', width=80)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        # Frame para os botões de ação
        frame_botoes = tk.Frame(frame_principal)
        frame_botoes.pack(pady=10)
        
        self.btn_abrir = tk.Button(frame_botoes, text="▶ Abrir Programa Selecionado", 
                                  command=self.abrir_programa, state=tk.DISABLED,
                                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_abrir.pack(side=tk.LEFT, padx=5)
        
        self.btn_abrir_local = tk.Button(frame_botoes, text="📂 Abrir Local do Arquivo", 
                                        command=self.abrir_local_arquivo, state=tk.DISABLED,
                                        bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.btn_abrir_local.pack(side=tk.LEFT, padx=5)
        
        self.btn_detalhes = tk.Button(frame_botoes, text="ℹ Detalhes", 
                                     command=self.mostrar_detalhes, state=tk.DISABLED,
                                     bg="#FF9800", fg="white", font=("Arial", 10, "bold"))
        self.btn_detalhes.pack(side=tk.LEFT, padx=5)
        
        # Bind para seleção na treeview
        self.tree.bind('<<TreeviewSelect>>', self.on_selecionar)
        self.tree.bind('<Double-Button-1>', lambda e: self.abrir_programa())
        
        # Status
        self.status = tk.Label(root, text="Carregando programas...", fg="blue", font=("Arial", 9))
        self.status.pack(pady=5)
        
        # Barra de progresso
        self.progresso = ttk.Progressbar(root, mode='indeterminate')
        self.progresso.pack(fill=tk.X, padx=10, pady=5)
        
        # Botão atualizar
        btn_atualizar = tk.Button(root, text="🔄 Atualizar Lista", command=self.carregar_programas,
                                 bg="#9E9E9E", fg="white", font=("Arial", 10))
        btn_atualizar.pack(pady=5)
        
        # Carrega os programas
        self.carregar_programas()
    
    def carregar_programas(self):
        """Carrega programas em thread separada"""
        self.progresso.start()
        self.status.config(text="Carregando lista de programas de múltiplas fontes...", fg="blue")
        self.btn_abrir.config(state=tk.DISABLED)
        self.btn_abrir_local.config(state=tk.DISABLED)
        self.btn_detalhes.config(state=tk.DISABLED)
        
        thread = threading.Thread(target=self._carregar_programas_thread)
        thread.start()
    
    def _carregar_programas_thread(self):
        """Carrega programas de múltiplas fontes"""
        programas = []
        programas_vistos = set()  # Para evitar duplicatas
        
        # 1. Carrega do registro Uninstall
        print("Carregando do registro Uninstall...")
        programas_uninstall = self._carregar_do_uninstall()
        for prog in programas_uninstall:
            chave_unica = f"{prog['nome']}_{prog['executavel']}"
            if chave_unica not in programas_vistos:
                programas_vistos.add(chave_unica)
                programas.append(prog)
        
        # 2. Carrega do AppPaths
        print("Carregando do AppPaths...")
        programas_apppaths = self._carregar_do_apppaths()
        for prog in programas_apppaths:
            chave_unica = f"{prog['nome']}_{prog['executavel']}"
            if chave_unica not in programas_vistos:
                programas_vistos.add(chave_unica)
                programas.append(prog)
        
        # 3. Carrega do Menu Iniciar (atalhos)
        print("Carregando do Menu Iniciar...")
        programas_menu = self._carregar_do_menu_iniciar()
        for prog in programas_menu:
            chave_unica = f"{prog['nome']}_{prog['executavel']}"
            if chave_unica not in programas_vistos:
                programas_vistos.add(chave_unica)
                programas.append(prog)
        
        # Ordena por nome
        programas.sort(key=lambda x: x['nome'].lower())
        
        self.programas = programas
        
        # Atualiza interface
        self.root.after(0, self._atualizar_lista)
    
    def _carregar_do_uninstall(self):
        """Carrega programas da chave Uninstall do registro"""
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
                        executavel = None
                        
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
                        
                        # Tenta encontrar o executável
                        try:
                            instal_location = winreg.QueryValueEx(subchave, "InstallLocation")[0]
                            if instal_location and os.path.exists(instal_location):
                                # Procura por .exe na pasta de instalação
                                for arquivo in os.listdir(instal_location):
                                    if arquivo.lower().endswith('.exe'):
                                        executavel = os.path.join(instal_location, arquivo)
                                        break
                        except:
                            pass
                        
                        if nome:
                            programas.append({
                                'nome': nome,
                                'descricao': descricao if descricao else '',
                                'executavel': executavel if executavel else '',
                                'fabricante': fabricante if fabricante else '',
                                'versao': versao if versao else '',
                                'fonte': 'Uninstall'
                            })
                        
                        winreg.CloseKey(subchave)
                    except:
                        pass
                winreg.CloseKey(chave)
            except:
                pass
        
        return programas
    
    def _carregar_do_apppaths(self):
        """Carrega programas da chave App Paths do registro"""
        programas = []
        caminhos = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths"
        ]
        
        for caminho in caminhos:
            try:
                chave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, caminho, 0, winreg.KEY_READ)
                
                for i in range(winreg.QueryInfoKey(chave)[0]):
                    try:
                        subchave_nome = winreg.EnumKey(chave, i)
                        subchave = winreg.OpenKey(chave, subchave_nome)
                        
                        # O nome da subchave geralmente é o nome do executável
                        executavel_nome = subchave_nome
                        
                        # Tenta obter o caminho completo do executável
                        caminho_executavel = None
                        try:
                            caminho_executavel = winreg.QueryValueEx(subchave, "")[0]
                        except:
                            # Se não encontrar o valor padrão, usa o próprio nome da chave
                            pass
                        
                        if caminho_executavel:
                            # Extrai o nome do programa do caminho do executável
                            nome_programa = os.path.splitext(executavel_nome)[0]
                            
                            # Tenta encontrar uma descrição melhor
                            descricao = f"Executável registrado no AppPaths"
                            
                            programas.append({
                                'nome': nome_programa,
                                'descricao': descricao,
                                'executavel': caminho_executavel,
                                'fabricante': '',
                                'versao': '',
                                'fonte': 'AppPaths'
                            })
                        
                        winreg.CloseKey(subchave)
                    except:
                        pass
                
                winreg.CloseKey(chave)
            except:
                pass
        
        return programas
    
    def _carregar_do_menu_iniciar(self):
        """Carrega programas das pastas do Menu Iniciar"""
        programas = []
        
        pastas = [
            os.path.join(os.environ.get('PROGRAMDATA', 'C:\\ProgramData'), 
                        'Microsoft\\Windows\\Start Menu\\Programs'),
            os.path.join(os.environ.get('APPDATA', ''), 
                        'Microsoft\\Windows\\Start Menu\\Programs')
        ]
        
        for pasta in pastas:
            if os.path.exists(pasta):
                try:
                    for item in os.listdir(pasta):
                        if item.lower().endswith('.lnk'):
                            nome = os.path.splitext(item)[0]
                            caminho_lnk = os.path.join(pasta, item)
                            
                            programas.append({
                                'nome': nome,
                                'descricao': 'Atalho do Menu Iniciar',
                                'executavel': caminho_lnk,
                                'fabricante': '',
                                'versao': '',
                                'fonte': 'Menu Iniciar'
                            })
                except:
                    pass
        
        return programas
    
    def _atualizar_lista(self):
        """Atualiza a lista na interface"""
        self.pesquisar()
        self.progresso.stop()
        self.status.config(text=f"Total: {len(self.programas)} programas carregados de múltiplas fontes", fg="green")
    
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
            # Trunca descrição se muito longa
            descricao = prog['descricao'][:100] + '...' if len(prog['descricao']) > 100 else prog['descricao']
            executavel = prog['executavel'][:100] + '...' if len(prog['executavel']) > 100 else prog['executavel']
            
            self.tree.insert('', 'end', text=str(i),
                           values=(prog['nome'], descricao, executavel,
                                  prog['fabricante'], prog['versao'], prog['fonte']))
        
        self.status.config(text=f"Resultados: {len(resultados)} de {len(self.programas)} programas")
    
    def on_selecionar(self, event):
        """Habilita botões quando um item é selecionado"""
        selecao = self.tree.selection()
        if selecao:
            self.btn_abrir.config(state=tk.NORMAL)
            self.btn_abrir_local.config(state=tk.NORMAL)
            self.btn_detalhes.config(state=tk.NORMAL)
        else:
            self.btn_abrir.config(state=tk.DISABLED)
            self.btn_abrir_local.config(state=tk.DISABLED)
            self.btn_detalhes.config(state=tk.DISABLED)
    
    def get_programa_selecionado(self):
        """Retorna o programa selecionado na treeview"""
        selecao = self.tree.selection()
        if not selecao:
            return None
        
        # Pega o índice da seleção
        item = selecao[0]
        valores = self.tree.item(item, 'values')
        
        # Procura o programa completo na lista
        nome = valores[0]
        for prog in self.programas:
            if prog['nome'] == nome:
                return prog
        return None
    
    def abrir_programa(self):
        """Abre o programa selecionado"""
        programa = self.get_programa_selecionado()
        if not programa:
            messagebox.showwarning("Aviso", "Selecione um programa primeiro!")
            return
        
        if not programa['executavel']:
            messagebox.showwarning("Aviso", f"Não foi possível encontrar o executável para:\n{programa['nome']}")
            return
        
        try:
            if programa['fonte'] == 'Menu Iniciar' and programa['executavel'].endswith('.lnk'):
                # Para atalhos .lnk, usamos start
                os.startfile(programa['executavel'])
            else:
                # Para executáveis normais
                subprocess.Popen([programa['executavel']], shell=True)
            
            self.status.config(text=f"Executando: {programa['nome']}", fg="green")
            # Reseta a cor da status após 2 segundos
            self.root.after(2000, lambda: self.status.config(fg="blue" if self.progresso.winfo_ismapped() else "green"))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir o programa:\n{str(e)}")
    
    def abrir_local_arquivo(self):
        """Abre a pasta onde o executável está localizado"""
        programa = self.get_programa_selecionado()
        if not programa:
            messagebox.showwarning("Aviso", "Selecione um programa primeiro!")
            return
        
        if not programa['executavel']:
            messagebox.showwarning("Aviso", f"Não foi possível encontrar o executável para:\n{programa['nome']}")
            return
        
        try:
            caminho = programa['executavel']
            pasta = os.path.dirname(caminho)
            
            if os.path.exists(pasta):
                # Abre a pasta no Explorer
                subprocess.Popen(f'explorer "{pasta}"')
                self.status.config(text=f"Abrindo pasta: {pasta}", fg="green")
            else:
                messagebox.showwarning("Aviso", f"A pasta não existe:\n{pasta}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a pasta:\n{str(e)}")
    
    def mostrar_detalhes(self):
        """Mostra detalhes completos do programa selecionado"""
        programa = self.get_programa_selecionado()
        if not programa:
            messagebox.showwarning("Aviso", "Selecione um programa primeiro!")
            return
        
        # Cria janela de detalhes
        detalhes = tk.Toplevel(self.root)
        detalhes.title(f"Detalhes - {programa['nome']}")
        detalhes.geometry("600x400")
        
        # Frame principal
        frame = tk.Frame(detalhes, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Mostra todas as informações
        tk.Label(frame, text="Nome:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W, pady=5)
        tk.Label(frame, text=programa['nome'], wraplength=450).grid(row=0, column=1, sticky=tk.W, pady=5)
        
        tk.Label(frame, text="Descrição:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky=tk.W, pady=5)
        tk.Label(frame, text=programa['descricao'] or "N/A", wraplength=450).grid(row=1, column=1, sticky=tk.W, pady=5)
        
        tk.Label(frame, text="Executável:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W, pady=5)
        tk.Label(frame, text=programa['executavel'] or "N/A", wraplength=450).grid(row=2, column=1, sticky=tk.W, pady=5)
        
        tk.Label(frame, text="Fabricante:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky=tk.W, pady=5)
        tk.Label(frame, text=programa['fabricante'] or "N/A", wraplength=450).grid(row=3, column=1, sticky=tk.W, pady=5)
        
        tk.Label(frame, text="Versão:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky=tk.W, pady=5)
        tk.Label(frame, text=programa['versao'] or "N/A", wraplength=450).grid(row=4, column=1, sticky=tk.W, pady=5)
        
        tk.Label(frame, text="Fonte:", font=("Arial", 10, "bold")).grid(row=5, column=0, sticky=tk.W, pady=5)
        tk.Label(frame, text=programa['fonte'], wraplength=450).grid(row=5, column=1, sticky=tk.W, pady=5)
        
        # Botões de ação na janela de detalhes
        frame_botoes = tk.Frame(detalhes)
        frame_botoes.pack(pady=20)
        
        if programa['executavel']:
            tk.Button(frame_botoes, text="Abrir Programa", command=lambda: self.abrir_programa() or detalhes.destroy(),
                     bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
            
            tk.Button(frame_botoes, text="Abrir Local", command=lambda: self.abrir_local_arquivo() or detalhes.destroy(),
                     bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_botoes, text="Fechar", command=detalhes.destroy,
                 bg="#9E9E9E", fg="white").pack(side=tk.LEFT, padx=5)

# Executar
if __name__ == "__main__":
    root = tk.Tk()
    app = PesquisaProgramasGUI(root)
    root.mainloop()