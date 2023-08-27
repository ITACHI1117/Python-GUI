from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')


my_notebook = tb.Notebook(root, bootstyle="dark")
my_notebook.pack(pady=20, padx=20)

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_label = tb.Label(tab1, text="Awsome Label")
my_label.pack(pady=20)

my_text = Text(tab1, width=80, height=20)
my_text.pack(pady=10,padx=10)

my_button = tb.Button(tab1, text="Click me",bootstyle="danger putline")

my_label2 = Label(tab2, text="This is tab 2")
my_label2.pack(pady=20)

# add frames to note book
my_notebook.add(tab1, text="Tab one")
my_notebook.add(tab2, text="Tab Two")

root.mainloop()
