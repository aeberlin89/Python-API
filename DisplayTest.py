from tkinter import *
import random
from PIL import Image

root = Tk()

n = 1
def callback(event):
    global n
    createButton(n, event.x, event.y)
    print ("clicked at", event.x, event.y)
    n = n+1

def createButton(num, x, y):
    colorDict = {
        0: "purple",
        1: 'red',
        2: "orange",
        3: "yellow",
        4: "green",
        5: "blue",
        6: "violet",
        7: "white",
        8: "black"
    }
    fg = colorDict[random.choice([1,2,3,4,5,6,7,8])]
    bg = colorDict[random.choice([1,2,3,4,5,6,7,8])]

    button = Label(text="Button " + str(num), fg=fg, bg=bg)
    button.place(x= x, y= y)


#Game List
frameTop = Frame(root)
frameTop.grid(columnspan=3, sticky='n')
game1 = Label(frameTop,text='Game1')
game2 = Label(frameTop,text='Game2')
game3 = Label(frameTop,text='Game3')
game1.grid(column=0)
game2.grid(row=0, column=1)
game3.grid(row=0, column=2)

#Away Team On Ice
frameLeft = Frame(root)
frameLeft.bind("<1>", callback)
frameLeft.grid(row=1, sticky='w')
label1 = Label(frameLeft,text='Player1')
label2 = Label(frameLeft,text='Player2')
label3 = Label(frameLeft,text='Player3')
label4 = Label(frameLeft,text='Player4')
label5 = Label(frameLeft,text='Player5')
label1.grid(row=0, sticky='w')
label2.grid(row=1, sticky='w')
label3.grid(row=2, sticky='w')
label4.grid(row=3, sticky='w')
label5.grid(row=4, sticky='w')


#ScoreBoard
frameMiddle = Frame(root, width=500, height=300, bg='black')
frameMiddle.grid(row=1, column=1)
frameMiddle.bind("<1>", callback)


#Test
#Use this for on ice player gen
frameTest = Frame(root)
frameTest.grid(row=1, column=3)
labelTest = []
for i in range(0,5):
    l = Label(frameTest,text='Player'+str(i+1))
    labelTest.append(l)
    labelTest[i].grid(row=(i))



#Home Team On Ice
frameRight = Frame(root)
frameRight.grid(row=1, column=2, sticky='w')
label1 = Label(frameRight,text='Player1')
label2 = Label(frameRight,text='Player2')
label3 = Label(frameRight,text='Player3')
label4 = Label(frameRight,text='Player4')
label5 = Label(frameRight,text='Player5')
label1.grid(row=0, sticky='w')
label2.grid(row=1, sticky='w')
label3.grid(row=2, sticky='w')
label4.grid(row=3, sticky='w')
label5.grid(row=4, sticky='w')













root.mainloop()
