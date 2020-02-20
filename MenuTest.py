from tkinter import *

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
frame = Frame(root, width=500, height=300, bg='black')
frame.grid()


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

root.mainloop()
