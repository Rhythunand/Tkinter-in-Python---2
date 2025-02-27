from tkinter import Tk, Label, Button, Entry, Frame, Text, Toplevel
root = Tk()
root.geometry('400x300')
root.title('main')

def topwin() :
  top = Toplevel()
  top.geometry('180x100')
  top.title('toplevel')
  l1 = Label(top, text='Thsi is toplevel window')
  l1.pack()

  top.mainloop()

l = Label(root,text='This is root window')
btn = Button(root, text='Click here to open another window', command=topwin)
root.mainloop()