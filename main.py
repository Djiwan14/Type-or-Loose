from tkinter import *
import time

# Window creation
window = Tk()
window.title("Type or loose it study helper app")
window.minsize(width=500, height=200)
window.config(bg="skyblue")
window.geometry("300x300+300+300")
# ________________________________Separation for frames________________________________________________________________
left_frame = Frame(window, width=200, height=200, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(window, width=325, height=200, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# ________________________________Main label creation__________________________________________________________________
mainLabel = Label(left_frame, text="Type or loose it", font=("Courier", 10, "bold"), fg="red")
mainLabel.grid(row=1, column=0, padx=5, pady=5)

# ____________________________________Image____________________________________________________________________________
try:
    image = PhotoImage(file="logo.png")
    original_image = image.subsample(3, 3)  # resize image using subsample
    Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)
except TclError:
    print("Image file not found or unable to load.")

# _________________________________Text entry__________________________________________________________________________
input_text = Text(right_frame, width=38, height=7)
input_text.grid(padx=5, pady=5)

# ___________________________Initialize last input time________________________________________________________________
last_input_time = time.time()


def update_last_input_time(event=None):
    global last_input_time
    last_input_time = time.time()


def check_input():
    global last_input_time
    current_time = time.time()

    # Check if 5 seconds have passed since the last input
    if current_time - last_input_time > 5:
        input_text.delete("1.0", "end")  # Clear text if no input in the last 5 seconds

    # Schedule the next check in 5 seconds
    window.after(5000, check_input)


# Bind the text widget to update last input time on any keypress
input_text.bind("<KeyPress>", update_last_input_time)

# Start periodic check
window.after(5000, check_input)


def quit_app():
    window.destroy()


# _____________________________________Button__________________________________________________________________________
quitButton = Button(left_frame, text="Quit", command=quit_app, width=17)
quitButton.grid()

window.mainloop()
