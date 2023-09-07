from tkinter import *
import ttkbootstrap as tb
import time

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK BootStrap")
# root.iconbitmap()
root.geometry('500x350')

def thing():

    # my_progress.step(20)
    my_progress['value'] +=10
    my_label.config(text=f"{my_progress['value']}")

def start():
    my_progress.start()


def stop():
    my_progress.stop()

def auto():
    for x in range(5):
        my_progress['value'] += 20
        my_label.config(text=f"{my_progress['value']}")
        #update 1 at a time
        root.update_idletasks()
        #increment afetr 1 second
        time.sleep(1)


my_progress =tb.Progressbar(root, bootstyle="danger", maximum=100, mode="determinate", length=300, value=0)
my_progress.pack(pady=20 ,padx=40)

my_frame = tb.Frame(root)
my_frame.pack(pady=20)

my_button = tb.Button(my_frame, text="Increment 20", bootstyle="info", command=thing)
my_button.grid(column=0, row=0, padx=10)

my_button = tb.Button(my_frame, text="Start", bootstyle="info", command=start)
my_button.grid(column=1, row=0, padx=10)

my_button = tb.Button(my_frame, text="Stop", bootstyle="info", command=stop)
my_button.grid(column=2, row=0, padx=10)

my_button = tb.Button(my_frame, text="Auto", bootstyle="info", command=auto)
my_button.grid(column=3, row=0, padx=10)

my_label = tb.Label(root, text="")
my_label.pack(pady=10)

root.mainloop()
