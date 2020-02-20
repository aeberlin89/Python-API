from tkinter import *
from tkinter import ttk

#create basic menu options
def NewFile():
    print('Creating new file...')

def OpenFile():
    print('Opening file...')

def Exit():
    print('Exiting...\nHave a nice day!')

def Undo():
    print('Undoing...')

def Redo():
    print('Redoing...')

root = Tk()
root.title('Menu Testing')

#create and place frame into new window
frame = Frame(root, width=500, height=300)
#frame.pack()

#create new window
aboutWindow = Toplevel()
aboutWindow.title('About')

#create menu objects for each window and assign each window a menu
mainMenu = Menu(root)
aboutMenu = Menu(root)
root.config(menu=mainMenu)
aboutWindow.config(menu=aboutMenu)

#create a sub menu to be placed in the main menu
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=NewFile)
fileMenu.add_command(label='Open', command=OpenFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=Exit)

#create a sub menu to be placed in the about menu
editMenu = Menu(aboutMenu)
aboutMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=Undo)
editMenu.add_command(label='Redo', command=Redo)

# *** Toolbar ***

#create frame for Toolbar
toolbar = Frame(root, bg='blue')
insertButton = ttk.Button(toolbar, text='Insert Image', command=OpenFile)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = ttk.Button(toolbar, text='Print', command=OpenFile)
printButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)
frame.pack()

# *** Statusbar ***

status = Label(root, text='Doing Nothing...', bd=1, relief=SUNKEN, anchor='w')
status.pack(side=BOTTOM, fill=X)

root.mainloop()
