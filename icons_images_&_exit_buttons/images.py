from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("My GUI")

#Images
my_img = ImageTk.PhotoImage(Image.open("images/green.jpg"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
