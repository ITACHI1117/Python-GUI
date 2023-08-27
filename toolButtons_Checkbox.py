from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def checker():
    if var1.get() == 1:
        my_label.config(text="Checked")
    else:
        my_label.config(text="UnChecked")


root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

#label
my_label = Label(text="Click check box")
my_label.pack(pady=(40,10))

var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="primary", text="Check me out", variable=var1, onvalue=1, offvalue=0, command=checker)
my_check.pack(pady=10)


#Tool Button

var2 =IntVar()
mycheck2 = tb.Checkbutton(bootstyle="success, toolbutton", text="Tool button", variable=var2, onvalue=1, offvalue=0, command=checker)
mycheck2.pack(pady=10)

#Tool Button

var3 =IntVar()
mycheck3= tb.Checkbutton(bootstyle="success, toolbutton, outline", text="Tool button", variable=var3, onvalue=1, offvalue=0, command=checker)
mycheck3.pack(pady=10)


#round toggle button
var4 =IntVar()
mycheck4= tb.Checkbutton(bootstyle="success,  round-toggle", text="Round toggle", variable=var4, onvalue=1, offvalue=0, command=checker)
mycheck4.pack(pady=10)

#square toggle button
var5 =IntVar()
mycheck5= tb.Checkbutton(bootstyle="warning,  square-toggle", text="Square toggle", variable=var5, onvalue=1, offvalue=0, command=checker)
mycheck5.pack(pady=10)




root.mainloop()