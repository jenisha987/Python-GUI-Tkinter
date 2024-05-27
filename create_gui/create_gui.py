from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel = Label(root, text="Hello World!")
name = Label(root, text="John Dan")
#Shoving it onto the screen
myLabel.pack()
name.pack()

root.mainloop()
