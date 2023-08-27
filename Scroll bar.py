from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')


# FFRAME
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

my_scroll = tb.Scrollbar(my_frame, orient='vertical', bootstyle="dark round",)
my_scroll.pack(side="right", fill="y")


my_text = Text(my_frame, width=30, height=30, yscrollcommand=my_scroll.set, wrap="none")
my_text.pack()

# confi scroll bar
my_scroll.config(command=my_text.yview)



root.mainloop()
