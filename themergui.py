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
    try: color = StringVar(value = th.currentProf[profName])
    except: color = StringVar(value=th.defaultFallback[profName])
    color.set(askcolor(color.get(), root)[1])
    if color.get() != 'None':
        unifiedWrite(profName, color.get())

# Variables that need to reinitialise on every update
def reInitVars(opcty, curshape, bgcolor, curcolor, useAcrylic):
    try : opcty = DoubleVar(value=th.currentProf['acrylicOpacity']) 
    except: opcty = DoubleVar(value=th.defaultFallback['acrylicOpacity'])

    try: curshape = StringVar(value=th.currentProf['cursorShape'])
    except: curshape = StringVar(value=th.defaultFallback['cursorShape'])

    try: bgcolor = StringVar(value=th.currentProf['background'])
    except: bgcolor = StringVar(value=th.defaultFallback['background']) 

    try: curcolor = StringVar(value=th.currentProf['cursorColor'])
    except: curcolor = StringVar(value=th.defaultFallback['cursorColor'])

    try: useAcrylic = BooleanVar(value=th.currentProf['useAcrylic'])
    except: useAcrylic = BooleanVar(value=th.defaultFallback['useAcrylic'])

    # print(bgcolor.get())



def selectShell(prof):
    th.currentProfName = prof
    th.currentProf = th.findProfile()
    # print(th.currentProfName)
    # print(th.currentProf)
    reInitVars(opcty, curshape, bgcolor, curcolor, useAcrylic)
    Tk.update(root)


# def rescue():
#     th.writeProfile(th.rescueProfile)

# Define variables 
opcty = DoubleVar(value=th.currentProf['acrylicOpacity'])
curshape = StringVar(value=th.currentProf['cursorShape'])
bgcolor = StringVar(value=th.currentProf['background'])
curcolor = StringVar(value=th.currentProf['cursorColor'])
useAcrylic = BooleanVar(value=th.currentProf['useAcrylic'])

reInitVars(opcty, curshape, bgcolor, curcolor, useAcrylic)    
prof = StringVar(value = th.allProfs[0])
cursorShapeList = [
    'bar',
    'emptyBox',
    'filledBox',
    'underscore',
    'vintage'
]

# Profile Selecter
OptionMenu(root,prof, *th.allProfs).grid(column = 0, columnspan = 2)
Button(root, text='Select Shell', command = lambda: selectShell(prof.get()) ).grid(column = 3) 

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