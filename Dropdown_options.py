from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *


def clicker():
    my_label.config(text=f"You clicked {my_combo.get()}!")


# bind function
def click_bind(e):
    my_label.config(text=f"You clicked {my_combo.get()}!")


root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

my_label = tb.Label(root, text="Hello World", font=("Helvetica, 18"))
my_label.pack(pady=20)

# Create dropDown options
days = ["Monday", "Tuesday", "Wenesday", "Thursday", "Friday", "Saturday", "Sunday"]

my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=20)

# set comobo default
my_combo.current(0)

# button
my_button = tb.Button(root, text="Click", command=clicker, bootstyle="danger")
my_button.pack(pady=20)

# Bind combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
