import asyncio
import tkinter as tk

from async_tkinter_loop import async_handler, async_mainloop


async def counter():
    i = 0
    while True:
        i += 1
        label.config(text=str(i))
        await asyncio.sleep(1.0)


root = tk.Tk()
label = tk.Label(root)
label.pack()

tk.Button(root, text="Start", command=async_handler(counter)).pack()

if __name__ == "__main__":
    async_mainloop(root)