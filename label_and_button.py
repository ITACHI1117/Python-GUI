from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

counter = 0
def changer():
    global counter
    counter+=1
    if counter %2 == 0:
        my_label.config(text="Hello World")
    else:
        my_label.config(text="Goodbye World")

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

# label,,,8
my_label = tb.Label(text="Hello World", font=("Helvetica", 28), bootstyle="danger")
my_label.pack(pady=50)
# button
my_button = tb.Button(text="Click me", bootstyle="sucess outline", command=changer)
my_button.pack(pady=20)

root.mainloop()