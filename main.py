from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

stuff = ["John", "April", "Bob", "Mary"]

#Spin box
my_spin = tb.Spinbox(root, bootstyle="success", from_=0, to=10, values=stuff)
my_spin.pack(pady=20)

root.mainloop()
