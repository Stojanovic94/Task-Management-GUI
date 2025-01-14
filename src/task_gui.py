import tkinter as tk
from tkinter import messagebox, ttk
from task import Task
from task_manager import TaskManager

class TaskGUI:
    def __init__(self, root, taskManager):
        self.root = root
        self.taskManager = taskManager
        self.root.title("Task Manager")
        
        # Dugmadi
        self.addButton = tk.Button(root, text="Dodaj zadatak", command=self.addTask)
        self.addButton.pack(pady=5)

        self.editButton = tk.Button(root, text="Izmeni zadatak", command=self.updateTask)
        self.editButton.pack(pady=5)

        self.deleteButton = tk.Button(root, text="Obriši zadatak", command=self.removeTask)
        self.deleteButton.pack(pady=5)

        # Tabela za zadatke
        self.taskTable = ttk.Treeview(root, columns=("Naziv", "Opis", "Status"), show="headings")
        self.taskTable.heading("Naziv", text="Naziv")
        self.taskTable.heading("Opis", text="Opis")
        self.taskTable.heading("Status", text="Status")
        self.taskTable.pack(pady=5)

        # Filter statusa
        self.filterMenu = ttk.Combobox(root, values=["u toku", "završeno", "na čekanju"])
        self.filterMenu.bind("<<ComboboxSelected>>", self.filterTasks)
        self.filterMenu.pack(pady=5)
        
        # Pretraga
        self.searchField = tk.Entry(root)
        self.searchField.pack(pady=5)
        self.searchField.bind("<KeyRelease>", self.searchTasks)

        self.showTasks()

    def showTasks(self):
        for row in self.taskTable.get_children():
            self.taskTable.delete(row)
        tasks = self.taskManager.getTasks()
        for task in tasks:
            self.taskTable.insert("", "end", values=(task.getName(), task.getDescription(), task.getStatus()))

    def addTask(self):
        def saveTask():
            name = nameEntry.get()
            description = descriptionEntry.get()
            status = statusVar.get()
            task = Task(name, description, status)
            self.taskManager.addTask(task)
            addWindow.destroy()
            self.showTasks()

        addWindow = tk.Toplevel(self.root)
        addWindow.title("Dodaj zadatak")
        
        tk.Label(addWindow, text="Naziv").pack(pady=5)
        nameEntry = tk.Entry(addWindow)
        nameEntry.pack(pady=5)

        tk.Label(addWindow, text="Opis").pack(pady=5)
        descriptionEntry = tk.Entry(addWindow)
        descriptionEntry.pack(pady=5)

        tk.Label(addWindow, text="Status").pack(pady=5)
        statusVar = tk.StringVar()
        statusMenu = ttk.Combobox(addWindow, textvariable=statusVar, values=["u toku", "završeno", "na čekanju"])
        statusMenu.pack(pady=5)

        saveButton = tk.Button(addWindow, text="Sačuvaj", command=saveTask)
        saveButton.pack(pady=5)

    def updateTask(self):
        selected = self.taskTable.selection()
        if not selected:
            messagebox.showwarning("Izbor", "Nema selektovanog zadatka")
            return
        
        taskName = self.taskTable.item(selected[0])["values"][0]
        task = next((task for task in self.taskManager.taskList if task.getName() == taskName), None)
        
        def update():
            name = nameEntry.get()
            description = descriptionEntry.get()
            status = statusVar.get()
            updatedTask = Task(name, description, status)
            self.taskManager.updateTask(taskName, updatedTask)
            updateWindow.destroy()
            self.showTasks()

        updateWindow = tk.Toplevel(self.root)
        updateWindow.title("Izmeni zadatak")
        
        tk.Label(updateWindow, text="Naziv").pack(pady=5)
        nameEntry = tk.Entry(updateWindow)
        nameEntry.insert(0, task.getName())
        nameEntry.pack(pady=5)

        tk.Label(updateWindow, text="Opis").pack(pady=5)
        descriptionEntry = tk.Entry(updateWindow)
        descriptionEntry.insert(0, task.getDescription())
        descriptionEntry.pack(pady=5)

        tk.Label(updateWindow, text="Status").pack(pady=5)
        statusVar = tk.StringVar()
        statusMenu = ttk.Combobox(updateWindow, textvariable=statusVar, values=["u toku", "završeno", "na čekanju"])
        statusMenu.set(task.getStatus())
        statusMenu.pack(pady=5)

        updateButton = tk.Button(updateWindow, text="Ažuriraj", command=update)
        updateButton.pack(pady=5)

    def removeTask(self):
        selected = self.taskTable.selection()
        if not selected:
            messagebox.showwarning("Izbor", "Nema selektovanog zadatka")
            return
        taskName = self.taskTable.item(selected[0])["values"][0]
        self.taskManager.removeTask(taskName)
        self.showTasks()

    def filterTasks(self, event):
        status = self.filterMenu.get()
        tasks = self.taskManager.getTasks(status)
        self.showTasks()

    def searchTasks(self, event):
        query = self.searchField.get().lower()
        filteredTasks = [task for task in self.taskManager.getTasks() if query in task.getName().lower()]
        self.showTasks(filteredTasks)
