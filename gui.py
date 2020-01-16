import themer as th
from tkinter import *

root = Tk()

def acryOpcty():
    th.currentProf['acrylicOpacity'] = opcty.get()
    print(th.currentProf)
opcty = DoubleVar()
acryOpctyScale = Scale(root, variable = opcty, orient = HORIZONTAL, from_ = 0, resolution = 0.01, to = 1.0)
acryOpctyScale.grid(row = 0, column = 0)

acryOpctyBttn = Button(root, text = 'Set opacity to 1', command=acryOpcty)
acryOpctyBttn.grid(row= 0, column = 1)


root.mainloop()