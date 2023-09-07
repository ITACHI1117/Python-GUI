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



def run():
    def stuff(x):
        my_menu.config(bootstyle={x})
        my_label.config(text=f"you selected {x}")

    my_menu = tb.Menubutton(root, bootstyle="warning", text="Things")
    my_menu.pack(pady=10)

    # create basic menu
    inside_menu = tb.Menu(my_menu)

    # Add Items to menu
    item_var = StringVar()
    for x in ['primary', 'secondary', 'danger', 'info', 'outline secondary', 'outline info', 'outline danger',
              'outline primary']:
        inside_menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x: stuff(x))

    # assiciate the inside with the menu button
    my_menu['menu'] = inside_menu

    my_label = tb.Label(root, text="")
    my_label.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':

    run()
