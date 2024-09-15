from tkinter import *

from sqlalchemy import column

# Window creation
window = Tk()
window.title("Type or loose it study helper app")
window.minsize(width=500, height=300)
# window.maxsize(width=1000, height=600)
window.config(bg="yellow")
window.geometry("300x300+300+300")
left_frame = Frame(window, width=200, height=200, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(window, width=325, height=200, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Main label creation
mainLabel = Label(left_frame, text="Type or loose it", font=("Courier", 10, "bold"), fg="red",)
mainLabel.grid(padx=5, pady=5)

# Text entry
input = Entry(right_frame, width=50)
input.grid(padx=5, pady=5)
window.mainloop()
