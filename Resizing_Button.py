from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *



root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

my_button.co

#style
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))

#Resizing button
my_button = tb.Button(text="Hello", width=40, bootstyle="success", style="success.Outline.TButton")
my_button.pack(pady=20)




root.mainloop()