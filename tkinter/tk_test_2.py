import random
import tkinter as tk

window = tk.Tk()
window.title("Welcome")
window.geometry("600x600")

# Functions


def phrase_generator():
    phrases = ["Hello", "What's up", "Aloha", "the cake is a lie"]
    name = str(entry_1.get())
    return phrases[random.randint(0, 3)] + " " + name


def phrase_display():
    greeting = phrase_generator()
    # this creates the text field
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=3)
    greeting_display.insert(tk.END, greeting)


# label
label_1 = tk.Label(text="welcome to my app")
label_1.grid(column=0, row=0)

label_2 = tk.Label(text="What is your name? ")
label_2.grid(column=0, row=1)

# Entries
entry_1 = tk.Entry()
entry_1.grid(column=1, row=1)

# Button
button_1 = tk.Button(text="Click Me", command=phrase_display)
button_1.grid(column=0, row=2)

window.mainloop()
