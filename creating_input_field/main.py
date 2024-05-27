from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="red", borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name:")  #gives default value inside the i/p field 

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name", padx=50, command=myClick)
myButton.pack()

myButton = Button(root, text="Click Me")

root.mainloop()