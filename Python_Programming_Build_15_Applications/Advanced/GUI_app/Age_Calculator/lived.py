from tkinter import *
from datetime import datetime

# Set the back- and foreground colors
bg_color = 'black'
fg_color = 'cyan'

# Main Window & Configuration
App = Tk()
App.title("Age Calculator")
App['background'] = bg_color
App.geometry('300x180')

# 'Enter Your DOB' Label
lbl = Label(App, text='Enter Your DOB:', background=bg_color,
            foreground=fg_color, font=('Courier', 12, 'bold'))
lbl.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Date Label & Entry widget
dayL = Label(App, text='Day: ', background=bg_color, foreground=fg_color)
dayE = Entry(App, background=bg_color, foreground='white', width=2)

# Month Label & Entry widget
monL = Label(App, text='Month: ', background=bg_color, foreground=fg_color)
monE = Entry(App, background=bg_color, foreground='white', width=2)

# Year Label & Entry widget
yrL = Label(App, text='Year: ', background=bg_color, foreground=fg_color)
yrE = Entry(App, background=bg_color, foreground='white', width=4)

# Placing the widgets using grid
dayL.grid(row=1, column=0)
dayE.grid(row=1, column=1)
monL.grid(row=1, column=2)
monE.grid(row=1, column=3)
yrL.grid(row=1, column=4)
yrE.grid(row=1, column=5)


def get_dob():
    day = int(dayE.get())
    month = int(monE.get())
    year = int(yrE.get())

    dob = datetime(year=year, month=month, day=day)
    return dob


# Finding Total days and creating it's Label
def find_days():
    dob = get_dob()
    time_now = datetime.now()
    time_dif = time_now - dob

    msg = Label(App, text='You have lived for ' + str(time_dif.days) + ' days!',
                background=bg_color, foreground='yellow')
    msg.grid(row=3, column=0, columnspan=3, pady=5)


# Finding Total seconds and creating it's Label
def find_sec():
    dob = get_dob()
    time_now = datetime.now()
    time_dif = time_now - dob

    msg = Label(App, text='You have lived for ' + str(time_dif.total_seconds()) + ' seconds!',
                background=bg_color, foreground='yellow')
    msg.grid(row=4, column=0, columnspan=6)


# Buttons for finding total days & seconds, and placing them
days_button = Button(App, text='Total days', command=find_days,
                     background=bg_color, foreground=fg_color)
days_button.grid(row=2, column=0, columnspan=3, pady=10)

sec_button = Button(App, text='Total seconds', command=find_sec,
                    background=bg_color, foreground=fg_color)
sec_button.grid(row=2, column=3, columnspan=3, pady=10)

App.mainloop()
