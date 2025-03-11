import asyncio
from tkinter import *
from tkinter import ttk
from async_tkinter_loop import async_handler, async_mainloop


root = Tk()
root.title("PyChat")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#mainframe_users_field= ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=300, height=600)
#mainframe_users_field.grid(column=0, row=0, sticky="w")

#user_frame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=50, height=35, padding="5 5 12 12")
#user_frame.grid(column=0, row=0, sticky="nwes", pady=2)

# Main chat frame frame that holds the text field.
main_textframe = ttk.Frame(mainframe, borderwidth=5, relief="ridge", padding="5 5 12 12")
main_textframe.grid(column=1, row=0, sticky="nwes", pady=2)

# Main chat field itself
main_textbox = Text(main_textframe, width=56, height=30, state=DISABLED)
main_textbox.grid(column=0, row=0, sticky="nwes", pady=2)

# User text input frame.
input_frame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", padding="5 10 12 12")
input_frame.grid(column=1, row=3, sticky="nwes", pady=2)

# User text input box
textbox = Text(input_frame, width=45, height=5)
textbox.grid(row=3, column=0, sticky="nwes", pady=2, padx=3)

# Send button
send_button = Button(input_frame, width=5, text="Send", anchor="center", activebackground="lime", highlightbackground="black",command="")
send_button.grid(row=3, column=3, sticky="e", pady=2, padx=1)


if __name__ == "__main__":
    async_mainloop(root)