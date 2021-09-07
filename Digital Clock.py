from tkinter import *
import time
from time import strftime

def time():
    string = str(strftime('%H:%M:%S %p'))
    lbl.config(text=string)
    lbl.after(1000, time)

top = Tk()
top.title("Digital Clock")
lbl = Label(top, font=('de-digital', 50, 'bold'), background='black', foreground='cyan')
lbl.pack(anchor='center')
time()
top.mainloop()
