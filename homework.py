from random import choice
from tkinter import RIDGE, Button, Tk, Label, messagebox

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")

user = Label(root, text = '')
user.pack()

computer = Label(root, text = '')
computer.pack()
l2 = Label(root, text = '')

def rock() :
  user['text'] = 'User choice is Rock'

  computer_l = ['Rock', 'Paper', 'Scissors', 'Rock', 'Paper', 'Scissors']
  computer_l_choice = choice(computer_l)
  if computer_l_choice == 'Rock' :
    l1['text'] = "It is a draw"
    l2['text'] = "The computer chose Rock"

  if computer_l_choice == 'Paper' :
    l1['text'] = "Computer wins the game"
    l2['text'] = "The computer chose Paper"

  if computer_l_choice == 'Scissors' :
    l1['text'] = "User wins the game"
    l2['text'] = "The computer chose Scissors"

def paper() :
  user['text'] = 'User choice is Paper'

  computer_l = ['Rock', 'Paper', 'Scissors', 'Rock', 'Paper', 'Scissors']
  computer_l_choice = choice(computer_l)
  if computer_l_choice == 'Rock' :
    l1['text'] = "User wins the game"
    l2['text'] = "The computer chose Rock"

  if computer_l_choice == 'Paper' :
    l1['text'] = "It is a draw"
    l2['text'] = "The computer chose Paper}"

  if computer_l_choice == 'Scissors' :
    l1['text'] = "Computer wins the game"
    l2['text'] = "The computer chose Scissors"

 
def scissors() :
  user['text'] = 'User choice is Scissors'

  computer_l = ['Rock', 'Paper', 'Scissors', 'Rock', 'Paper', 'Scissors']
  computer_l_choice = choice(computer_l)
  if computer_l_choice == 'Rock' :
    l1['text'] = "Computer wins the game"
    l2['text'] = "The computer chose Rock"

  if computer_l_choice == 'Paper' :
    l1['text'] = "User wins the game"
    l2['text'] = "The computer chose Paper"

  if computer_l_choice == 'Scissors' :
    l1['text'] = "It is a draw"
    l2['text'] = "The computer chose Scissors"

rock = Button(root, text="Rock", font=('Bold'), width=50, height=2, relief=RIDGE, command=rock)
paper = Button(root, text='Paper', font=('Bold'), width=50, height=2, relief=RIDGE, command=paper)
scissors = Button(root, text= 'Scissors', font=('Bold'), width=50,height=2,relief=RIDGE, command=scissors)
play_again = Button(root, text= 'Play Again', font=('Bold'), bg = 'black', fg = 'white', width=50,height=2,relief=RIDGE)


rock.pack()
paper.pack()
scissors.pack()
play_again.pack()


l1 = Label(root, text="", font=('Helvetica', 17, 'bold'))
l1.pack()
root.mainloop()