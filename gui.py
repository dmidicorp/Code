import asyncio
from tkinter import *
from tkinter import ttk
from async_tkinter_loop import async_handler, async_mainloop


root = Tk()
root.title("PyChat")
#label = tk.Label(root)
#label.pack()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
textbox = Text(root, width=120, height=10)

#tk.Button(root, text="Start", command=async_handler(counter)).pack()

if __name__ == "__main__":
    async_mainloop(root)