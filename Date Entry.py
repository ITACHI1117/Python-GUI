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


def datey():
    my_label.config(text=f"You Picked: {my_date.entry.get()}")

def thing():
    cal =Querybox
    my_label.config(text=f"You Picked: {cal.get_date()}")


#     this returns a sting not a date time object
# changed the default start date with (start date)
# changed the first week day (firstweekday)
my_date = tb.DateEntry(root, bootstyle="dark", firstweekday=0, startdate=date(2023, 2, 14))
my_date.pack(pady=20)

my_button = tb.Button(root, text="Get Data", bootstyle="danger outline", command=datey)
my_button.pack(pady=10)

my_button2 = tb.Button(root, text="Get Calender", bootstyle="success outline", command=thing)
my_button2.pack(pady=10)

my_label = tb.Label(root, text="You Picked", )
my_label.pack(pady=10)

root.mainloop()
