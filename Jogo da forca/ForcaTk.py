import tkinter as tk
from tkinter import messagebox
import random

class JogoDaForca:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")
        self.palavra = self.escolher_palavra()
        self.palavra_oculta = ['_'] * len(self.palavra)
        self.letras_tentadas = []
        self.tentativas = 0
        
        self.frame_palavra = tk.Frame(self.master)
        self.frame_palavra.pack()
        
        self.label_palavra = tk.Label(self.frame_palavra, text=' '.join(self.palavra_oculta))
        self.label_palavra.pack()
        
        self.label_letras = tk.Label(self.master, text="Letras tentadas: ")
        self.label_letras.pack()
        
        self.entry_letra = tk.Entry(self.master)
        self.entry_letra.pack()
        
        self.button_verificar = tk.Button(self.master, text="Verificar", command=self.verificar_letra)
        self.button_verificar.pack()
        
        self.canvas_forca = tk.Canvas(self.master, width=300, height=300)
        self.canvas_forca.pack()
        
        self.exibir_forca()

    def escolher_palavra(self):
        palavras = ['desenvolvimento', 'tecnologia', 'logica', 'progrmacao', 'python', 'hardware', 'software', 'teclado', 'aplicacao', 'meta', 'ciencia', 'web']
        return random.choice(palavras)

    def exibir_forca(self):
        # Lista de strings representando as fases da forca
        fases_forca = [
            "   ____\n"
            "  |        |\n"
            "           |\n"
            "           |\n"
            "           |\n"
            "           |\n"
            " _____|_____",
            "   ____\n"
            "  |        |\n"
            "  O       |\n"
            "           |\n"
            "           |\n"
            "           |\n"
            " _____|_____",
            "   ____\n"
            "  |        |\n"
            "  O       |\n"
            "  |        |\n"
            "           |\n"
            "           |\n"
            " _____|_____",
            "   ____\n"
            "  |        |\n"
            "  O       |\n"
            " /|        |\n"
            "           |\n"
            "           |\n"
            " _____|_____",
            "   ____\n"
            "  |        |\n"
            "  O       |\n"
            " /|\       |\n"
            "           |\n"
            "           |\n"
            " _____|_____",
            "   ____\n"
            "  |        |\n"
            "  O       |\n"
            " /|\       |\n"
            " /         |\n"
            "           |\n"
            " _____|_____",
            "   ____\n"
            "  |        |\n"
            "  O       |\n"
            " /|\       |\n"
            " / \       |\n"
            "           |\n"
            " _____|_____"
        ]
        # Limpa o canvas
        self.canvas_forca.delete("all")
        # Desenha a fase atual da forca
        self.canvas_forca.create_text(150, 150, text=fases_forca[self.tentativas], font=("Arial", 16), anchor="center")

    def verificar_letra(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if letra in self.letras_tentadas:
            messagebox.showwarning("Letra repetida", "Você já tentou esta letra. Tente outra.")
            return

        self.letras_tentadas.append(letra)

        if letra in self.palavra:
            messagebox.showinfo("Letra correta", "Letra correta!")
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.palavra_oculta[i] = letra
        else:
            messagebox.showerror("Letra incorreta", "Letra incorreta!")
            self.tentativas += 1
            self.exibir_forca()

        self.label_palavra.config(text=' '.join(self.palavra_oculta))
        self.label_letras.config(text="Letras tentadas: " + ' '.join(self.letras_tentadas))

        if '_' not in self.palavra_oculta:
            messagebox.showinfo("Parabéns!", "Você venceu!")
            self.reiniciar_jogo()

        if self.tentativas == 6:
            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era: {self.palavra}")
            self.reiniciar_jogo()

    def reiniciar_jogo(self):
        self.palavra = self.escolher_palavra()
        self.palavra_oculta = ['_'] * len(self.palavra)
        self.letras_tentadas = []
        self.tentativas = 0
        self.label_palavra.config(text=' '.join(self.palavra_oculta))
        self.label_letras.config(text="Letras tentadas: ")
        self.exibir_forca()

def main():
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()

if __name__ == "__main__":
    main()