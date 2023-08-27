from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')


def click():
    my_label.config(text=f"You Selected: {my_toppings.get()}")

toppings = ["cheese","veggie", "pepper"]

my_toppings = StringVar()

for toppings in toppings:
    tb.Radiobutton(root, bootstyle="secondary", variable=my_toppings, text=toppings, command=click, value=toppings).pack(pady=20)

# button
my_button = tb.Button(root, text="Click", command=click)
my_button.pack(pady=20)

my_label = tb.Label(root, text="you selected: ")
my_label.pack(pady=20)

# actual radio button button

rb1 = tb.Radiobutton(root, bootstyle="info toolbutton", variable=my_toppings, text="radio button1", command=click, value="ra 1")
rb1.pack(pady=20)
rb2 = tb.Radiobutton(root, bootstyle="info toolbutton outline", variable=my_toppings, text="radio button1", command=click, value="ra 2")
rb2.pack(pady=20)




root.mainloop()
