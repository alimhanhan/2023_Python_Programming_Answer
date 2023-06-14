from tkinter import *

window = Tk()
colors = ['#000000', '#FFC0CB', '#800080', '#FFFF00', '#0000FF', '#808080']

r = 0
for c in colors:
    Label(window, text=c, relief=RIDGE, width=15).grid(row=r, column=0)
    Button(window, bg=c, width=10).grid(row=r, column=1)
    r = r + 1

window.mainloop()