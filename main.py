from tkinter import *

from sqlalchemy import column

# Window creation
window = Tk()
window.title("Type or loose it study helper app")
window.minsize(width=500, height=300)
# window.maxsize(width=1000, height=600)
window.config(bg="yellow")
window.geometry("300x300+300+300")

# Main label creation
mainLabel = Label(text="Type or loose it", font=("Courier", 20, "bold"), bg="yellow", fg="red")
mainLabel.grid(padx=125, pady=10)

# Text entry
input = Entry(width=50)
input.grid()
window.mainloop()
