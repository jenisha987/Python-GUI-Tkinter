from tkinter import *

root = Tk()
root.title("My GUI")

#Exit Button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
