from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *


root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')


def starter():
    my_guage.start()
def stoper():
    my_guage.stop()
def incrementer():
    my_guage.step(+10)
    my_label.config(text=f"Position {my_guage.variable.get() +10}")


my_guage = tb.Floodgauge(root, bootstyle="success", font=("Helvetica",18),
                         mask="Pos: {}%", maximum=80,orient="horizontal", value=10, mode="determinate")
my_guage.pack(pady=10, fill=X, padx=20)

#button
start_button = tb.Button(root, text="Start", bootstyle="danger outline", command=starter)
start_button.pack(pady=20)

stop_button = tb.Button(root, text="Stop", bootstyle="danger outline", command=stoper)
stop_button.pack(pady=20)

increment_button = tb.Button(root, text="Add", bootstyle="danger outline", command=incrementer)
increment_button.pack(pady=20)

my_label = tb.Label(root, text="Position")
my_label.pack(pady=20)

root.mainloop()
