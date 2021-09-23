from tkinter import *
from random import randint

App = Tk()
App.title("Dice Roller")
App.geometry('280x200')
App['background'] = 'grey'

# Dice unicode characters dictionary
Dice = {
    # 0: '🎲',
    1: '\u2680',
    2: '\u2681',
    3: '\u2682',
    4: '\u2683',
    5: '\u2684',
    6: '\u2685'
}


# First dice character to show when the app starts
first_no = randint(1,6)
lbl = Label(App, text=Dice[first_no], font=('Times', 100), background='grey', foreground='white')
lbl.grid(row=0, column=0, padx=90)


# Choose number from 1 - 6 randomly and display it
def roll():
    dice_choice = randint(1, 6)
    dice_lbl = Label(App, text=Dice[dice_choice], font=('Times', 100), background='grey', foreground='white')
    dice_lbl.grid(row=0, column=0, padx=90)


# Roll button
roll_button = Button(App, text='Roll', command=roll)
roll_button.grid()
roll_button.config(width=6)

App.mainloop()
