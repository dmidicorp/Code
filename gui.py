import asyncio
from tkinter import *
from tkinter import ttk
from async_tkinter_loop import async_handler, async_mainloop

# Main application window, holding our main application frame.
root = Tk()
root.title("PyChat")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Main application frame that holds all other frames.
mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


# Main chat frame frame that holds the text field.
main_textframe = ttk.Frame(mainframe, borderwidth=5, relief="ridge", padding="10 5 12 12")
main_textframe.grid(column=1, row=0, sticky="nwes", pady=2)

# Main chat field itself
main_textbox = Text(main_textframe, width=56, height=30, state=DISABLED)
main_textbox.grid(column=0, row=0, sticky="nwes", pady=2)

# User text input frame.
input_frame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", padding="10 10 12 12")
input_frame.grid(column=1, row=3, sticky="nwes", pady=2)

# User text input box
textbox = Text(input_frame, width=45, height=5)
textbox.grid(row=3, column=0, sticky="nwes", pady=2, padx=5)

# Send button
send_button = Button(input_frame, width=5, text="Send", anchor="center", activebackground="lime", highlightbackground="black",command="")
send_button.grid(row=3, column=3, sticky="nwes", pady=2, padx=5)


if __name__ == "__main__":
    async_mainloop(root)