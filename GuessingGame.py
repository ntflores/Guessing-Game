# took the idea for a guessing game from a website and then made it into a GUI using tkinter

# importing modules
from tkinter import *
import random

# creating root window
root = Tk()

# root window title and dimensions
root.title("Guessing Game")
root.geometry("300x300")

# makes it so it can not be expanded
root.resizable(0, 0)

# adding a label to the root window
label = Label(root, text ="Enter an integer from 1 to 10: ")
label.grid()

# adding an entry field
entry = Entry(fg="blue", bg="white", width=20)
entry.grid()

# guessing game
def game():
    # makes n a random integer between 1 and 10
    n = random.randint(1, 10)

    # takes the value from the entry field and assigns it to the string guess
    guess = entry.get()

    # change guess from string to an integer
    guess = int(guess)

    # while loop to run the program until the user makes the correct guess
    while n != "guess":
        if guess < n:
            label.configure(text = "Guess is low. Guess again: ")
            entry.delete(0, END)
            guess = entry.get()
        elif guess > n:
            label.configure(text = "Guess is high. Guess again: ")
            entry.delete(0, END)
            guess = entry.get()
        else:
            label.configure(text = "You guessed correctly!")
            break

# makes the "enter" button
btn = Button(root, text = "Enter", fg = "blue", command = game)

# button placement
btn.grid(column = 2, row = 1)

root.mainloop()