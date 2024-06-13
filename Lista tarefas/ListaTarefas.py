import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.task_label = tk.Label(root, text="Tarefa:")
        self.task_label.pack()
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(root)
        self.tasks_listbox.pack()

        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack()

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()