from task_manager import TaskManager
from task_gui import TaskGUI
import tkinter as tk

def main():
    root = tk.Tk()
    taskManager = TaskManager()
    gui = TaskGUI(root, taskManager)
    root.mainloop()

if __name__ == "__main__":
    main()
