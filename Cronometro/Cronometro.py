import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.label.pack()

        self.start_button = tk.Button(root, text="Iniciar", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Parar", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset)
        self.reset_button.pack()

        self.update_time()

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1
            time_str = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            self.label.config(text=time_str)
        self.root.after(1000, self.update_time)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()