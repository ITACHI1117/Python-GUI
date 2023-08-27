from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *


root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

def speak():
    my_label.config(text=f"you typed: {my_entry.get()}")

# uses characters not px
#Entry widigt
my_entry= tb.Entry(root, bootstyle="success", font=("Helvetica", 18),foreground="yellow", width=5, show="*")
my_entry.pack(pady=50)

#button
my_button = tb.Button(root, bootstyle="danger outline", text="Click me" ,command=speak)
my_button.pack(pady=20)

my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
