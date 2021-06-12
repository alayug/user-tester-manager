#!/usr/bin/python
import tkinter as tk
from services.insertTask import insert_task
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.insert_task_section = tk.Button(self)
        self.insert_task_section["text"] = "Insert Task"
        self.insert_task_section["command"] = self.insert_task
        self.insert_task_section.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def insert_task(self):
        insert_task(1,"New Task")

root = tk.Tk()
app = Application(master=root)
app.mainloop()