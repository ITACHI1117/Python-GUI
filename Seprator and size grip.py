from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')


label1 = tb.Label(root, text="label 1", bootstyle="light")
label1.pack(pady=40)

my_sep = tb.Separator(root, bootstyle="light", orient="horizontal")
my_sep.pack(pady=10, fill="x", padx=100)

label2 = tb.Label(root, text="label 1", bootstyle="light")
label2.pack(pady=40)

#Size grip
my_sizegrip = tb.Sizegrip(root, bootstyle="info")
my_sizegrip.pack(anchor="se", fill="both", expand="True")

root.mainloop()
