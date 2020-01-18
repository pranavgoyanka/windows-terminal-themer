import themer as th
from tkinter import *
from tkcolorpicker import askcolor

root = Tk()

# def acryOpcty():
#     th.currentProf['acrylicOpacity'] = opcty.get()
#     th.writeProfile(th.currentProf)

# def cursorShape():
#     th.currentProf['cursorShape'] = str(curshape.get())
#     # print(th.currentProf)
#     th.writeProfile(th.currentProf)

def unifiedWrite(profName, val):
    th.currentProf[profName] = val
    th.writeProfile(th.currentProf)

def pickColor(profName):
    color = StringVar(value = th.currentProf[profName])
    color.set(askcolor(color.get(), root)[1])
    if color.get() != 'None':
        unifiedWrite(profName, color.get())

# def rescue():
#     th.writeProfile(th.rescueProfile)

# Define variables
opcty = DoubleVar(value=th.currentProf['acrylicOpacity'])
curshape = StringVar(value=th.currentProf['cursorShape'])
bgcolor = StringVar(value=th.currentProf['background'])
curcolor = StringVar(value=th.currentProf['cursorColor'])
useAcrylic = BooleanVar(value=th.currentProf['useAcrylic'])
cursorShapeList = [
    'bar',
    'emptyBox',
    'filledBox',
    'underscore',
    'vintage'
]

# Use Acrylic
Checkbutton(root, text='Enable/Disable Acrylic (Blur Effect)', variable=useAcrylic, command=lambda: unifiedWrite('useAcrylic', useAcrylic.get())).grid(column=0, columnspan=3)

# Acrylic Opacity
Label(root, text='Acrylic Opacity (Only effective if Acrylic is Enabled)').grid(columnspan=3)
acryOpctyScale = Scale(root, variable = opcty, orient = HORIZONTAL, from_ = 0, resolution = 0.01, to = 1.0)
acryOpctyScale.grid(column = 0)
acryOpctyBttn = Button(root, text = 'Set', command=lambda: unifiedWrite('acrylicOpacity', opcty.get()))
acryOpctyBttn.grid(column=2, rowspan=4)

# Cursor Shape
Label(root, text='Cursor Shape').grid(column=0, columnspan=3)
for i in range(len(cursorShapeList)):
    R = Radiobutton(root, text=cursorShapeList[i], variable=curshape, value=cursorShapeList[i], command=lambda: unifiedWrite('cursorShape', curshape.get()))
    R.grid(column=0, columnspan = 3)
    
# Background Color
Label(root, text='Background Color').grid(column=0)
Button(root, text='Color Picker', command=lambda: pickColor('background')).grid(column=1)

# Cursor Color
Label(root, text='Cursor Color').grid(column=0)
Button(root, text='Color Picker', command=lambda: pickColor('cursorColor')).grid(column=1)

# Font Size
Label(root, text='Font Size').grid(column=0)
fontsize = Entry(root)
fontsize.insert(0, th.currentProf['fontSize'])
fontsize.grid(column=1)
Button(root, text='Set', command=lambda: unifiedWrite('fontSize', int(fontsize.get()))).grid(column=2)

# Rescue Profile 
Button(root, text='Rescue Profile (if something breaks)', state=DISABLED).grid()

# Exit Button
Button(root, text="Quit", command=root.destroy).grid()

root.mainloop()