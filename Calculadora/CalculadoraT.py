import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.label_num1 = tk.Label(self.frame, text="Número 1:")
        self.label_num1.grid(row=0, column=0)
        self.entry_num1 = tk.Entry(self.frame)
        self.entry_num1.grid(row=0, column=1)

        self.label_num2 = tk.Label(self.frame, text="Número 2:")
        self.label_num2.grid(row=1, column=0)
        self.entry_num2 = tk.Entry(self.frame)
        self.entry_num2.grid(row=1, column=1)

        self.label_resultado = tk.Label(self.frame, text="Resultado:")
        self.label_resultado.grid(row=2, column=0)
        self.entry_resultado = tk.Entry(self.frame, state="readonly")
        self.entry_resultado.grid(row=2, column=1)

        self.button_adicionar = tk.Button(self.frame, text="Adicionar", command=self.adicionar)
        self.button_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

        self.button_subtrair = tk.Button(self.frame, text="Subtrair", command=self.subtrair)
        self.button_subtrair.grid(row=4, column=0, columnspan=2, pady=5)

        self.button_multiplicar = tk.Button(self.frame, text="Multiplicar", command=self.multiplicar)
        self.button_multiplicar.grid(row=5, column=0, columnspan=2, pady=5)

        self.button_dividir = tk.Button(self.frame, text="Dividir", command=self.dividir)
        self.button_dividir.grid(row=6, column=0, columnspan=2, pady=5)

    def adicionar(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            resultado = num1 + num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
            self.entry_resultado.config(state="readonly")
        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos.")

    def subtrair(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            resultado = num1 - num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
            self.entry_resultado.config(state="readonly")
        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos.")

    def multiplicar(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            resultado = num1 * num2
            self.entry_resultado.config(state="normal")
            self.entry_resultado.delete(0, tk.END)
            self.entry_resultado.insert(0, resultado)
            self.entry_resultado.config(state="readonly")
        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos.")

    def dividir(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            if num2 == 0:
                messagebox.showerror("Erro", "Não é possível dividir por zero.")
            else:
                resultado = num1 / num2
                self.entry_resultado.config(state="normal")
                self.entry_resultado.delete(0, tk.END)
                self.entry_resultado.insert(0, resultado)
                self.entry_resultado.config(state="readonly")
        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()