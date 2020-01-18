import themer as th
from tkinter import *

root = Tk()

def acryOpcty():
    th.currentProf['acrylicOpacity'] = opcty.get()
    th.writeProfile(th.currentProf)

def cursorShape():
    th.currentProf['cursorShape'] = str(curshape.get())
    # print(th.currentProf)
    th.writeProfile(th.currentProf)

# Define variables
opcty = DoubleVar(value=th.currentProf['acrylicOpacity'])
curshape = StringVar(value=th.currentProf['cursorShape'])
cursorShapeList = [
    'bar',
    'emptyBox',
    'filledBox',
    'underscore',
    'vintage'
]


# Frame
LabelFrame(root, text='Windows Terminal Themer',padx=5, pady=6).grid(padx=5, pady=5)

# Acrylic Opacity
acryOpctyScale = Scale(root, variable = opcty, orient = HORIZONTAL, from_ = 0, resolution = 0.01, to = 1.0)
acryOpctyScale.grid(row = 0, column = 0)
acryOpctyBttn = Button(root, text = 'Set', command=acryOpcty)
acryOpctyBttn.grid(row= 0, column = 1)

# Cursor Shape
Label(root, text='Cursor Shape').grid()
for i in range(len(cursorShapeList)):
    R = Radiobutton(root, text=cursorShapeList[i], variable=curshape, value=cursorShapeList[i], command=cursorShape)
    R.grid()
    



root.mainloop()