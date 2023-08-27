from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from datetime import date
from ttkbootstrap.dialogs import  Querybox

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

def thing():
    pass


my_frame = Frame(root) #bootstyle="light")
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, text="Click", bootstyle="dark", command=thing)
my_button.pack(pady=10)

my_label = tb.Label(root,text="Hello here", font=("Helvetica", 18) )
my_label.pack(pady=20)


root.mainloop()
