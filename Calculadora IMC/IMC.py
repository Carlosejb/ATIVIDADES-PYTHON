import tkinter as tk

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        self.label_height = tk.Label(root, text="Altura (m):")
        self.label_height.pack()
        self.entry_height = tk.Entry(root)
        self.entry_height.pack()

        self.label_weight = tk.Label(root, text="Peso (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(root)
        self.entry_weight.pack()

        self.calculate_button = tk.Button(root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            bmi = weight / (height ** 2)
            self.show_bmi_category(bmi)
        except ValueError:
            self.result_label.config(text="Valores inválidos. Digite números válidos.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 24.9 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        self.result_label.config(text=f"IMC: {bmi:.2f} ({category})")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()