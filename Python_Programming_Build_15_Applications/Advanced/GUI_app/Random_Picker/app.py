from tkinter import *
from random import sample, choice

App = Tk()                          # Graphical user interface (window)
App.title('Element picker')         # Title in the header of the window
App.geometry('400x150')             # Make the window size accordingly (in pixels)
App['background'] = 'grey'

# Create a user input field
userInput = Entry(App, background='white', foreground='black', borderwidth=2, width=30)
userInput.grid(row=0, column=0, columnspan=2, padx=100, pady=10)

# Make a slider/scale for user to chose how many numbers to output
no_choice = IntVar()
slider = Scale(App, from_=1, to=5, variable=no_choice, orient=HORIZONTAL)
slider.grid(row=1, column=0, columnspan=2, padx=25, pady=5)


def pick():     # Show user input message when button is clicked
    user_msg = (userInput.get()).split(',')

    if no_choice.get() != 1:
        elements = sample(user_msg, no_choice.get())
        ret_str = ''
        for i in elements:
            ret_str += ' ' + i
        chosen = 'Choice:\n' + str(ret_str)
    else:
        # Retrieving one element from the input string (using 'choice')
        chosen = 'Choice:\n' + str(choice(user_msg))

    # Create a separate window for displaying the output
    output_window = Toplevel()
    output_window.title('Output')
    output_window.geometry('450x100')
    output_window['background'] = 'grey'

    msg = Label(output_window, text=chosen, font=('Courier', 14), width=35)
    msg.grid(row=0, column=0, padx=20, pady=20)

    # Make cancel button enabled when user has activated the program
    if quit_button['state'] == DISABLED:
        quit_button['state'] = NORMAL


# Button for choosing (outputting) a random number
chose_button = Button(App, text='Choose', command=pick, background='green',
                      foreground='white', relief='raised', borderwidth=2, width=10)
chose_button.grid(row=2, column=0, pady=5)

# Button for closing the application (disabled until user activates program)
quit_button = Button(App, text='Close', command=App.quit, state=DISABLED, background='red',
                     foreground='white', relief='raised', borderwidth=2, width=10)
quit_button.grid(row=2, column=1,pady=5)

# Open up the 'window' interface
App.mainloop()
