import tkinter as tk
from tkinter import messagebox

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            messagebox.showwarning("Contato Existente", f"O contato {nome} já existe na agenda.")
        else:
            self.contatos[nome] = telefone
            messagebox.showinfo("Contato Adicionado", f"Contato {nome} adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            messagebox.showinfo("Contato Removido", f"Contato {nome} removido com sucesso.")
        else:
            messagebox.showwarning("Contato Não Encontrado", f"Contato {nome} não encontrado na agenda.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            messagebox.showinfo("Contato Encontrado", f"Nome: {nome}\nTelefone: {self.contatos[nome]}")
        else:
            messagebox.showwarning("Contato Não Encontrado", f"Contato {nome} não encontrado na agenda.")

    def listar_contatos(self):
        if not self.contatos:
            messagebox.showinfo("Agenda Vazia", "A agenda está vazia.")
        else:
            lista_contatos = "Lista de contatos:\n"
            for nome, telefone in self.contatos.items():
                lista_contatos += f"Nome: {nome}, Telefone: {telefone}\n"
            messagebox.showinfo("Lista de Contatos", lista_contatos)

class InterfaceAgenda:
    def __init__(self, master):
        self.master = master
        self.master.title("Agenda Telefônica")
        self.agenda = AgendaTelefonica()

        self.frame_adicionar = tk.Frame(self.master)
        self.frame_adicionar.pack(pady=10)

        self.label_nome = tk.Label(self.frame_adicionar, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame_adicionar)
        self.entry_nome.grid(row=0, column=1)

        self.label_telefone = tk.Label(self.frame_adicionar, text="Telefone:")
        self.label_telefone.grid(row=1, column=0)
        self.entry_telefone = tk.Entry(self.frame_adicionar)
        self.entry_telefone.grid(row=1, column=1)

        self.button_adicionar = tk.Button(self.frame_adicionar, text="Adicionar Contato", command=self.adicionar_contato)
        self.button_adicionar.grid(row=2, columnspan=2)

        self.frame_operacoes = tk.Frame(self.master)
        self.frame_operacoes.pack(pady=10)

        self.button_remover = tk.Button(self.frame_operacoes, text="Remover Contato", command=self.remover_contato)
        self.button_remover.grid(row=0, column=0, padx=5)

        self.button_pesquisar = tk.Button(self.frame_operacoes, text="Pesquisar Contato", command=self.pesquisar_contato)
        self.button_pesquisar.grid(row=0, column=1, padx=5)

        self.button_listar = tk.Button(self.frame_operacoes, text="Listar Contatos", command=self.listar_contatos)
        self.button_listar.grid(row=0, column=2, padx=5)

    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        self.agenda.adicionar_contato(nome, telefone)

    def remover_contato(self):
        nome = self.entry_nome.get()
        self.agenda.remover_contato(nome)

    def pesquisar_contato(self):
        nome = self.entry_nome.get()
        self.agenda.pesquisar_contato(nome)

    def listar_contatos(self):
        self.agenda.listar_contatos()

def main():
    root = tk.Tk()
    app = InterfaceAgenda(root)
    root.mainloop()

if __name__ == "__main__":
    main()