from tkinter import Tk, Label, Button, Entry, Frame, Text
from PIL import Image, ImageTk
root = Tk()
root.title('image')
root.geometry('400x400')

upload = Image.open('img.jpeg')
image = ImageTk.PhotoImage(upload)

label1 = Label(root, image = image , height=350, width=300)
label1.place(x=50, y=0)
label2 = Label(root, text = 'This is how to add image to Tkinter window')
label2.place(x=40, y=360)

root.mainloop()