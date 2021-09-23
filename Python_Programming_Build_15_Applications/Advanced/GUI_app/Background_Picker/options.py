from tkinter import *

App = Tk()
App.title('Background Picker')
App.geometry('300x180')
App['background'] = 'grey'

menu_ch = StringVar()
options = ['Grey', 'Red', 'Blue', 'Green', 'Yellow', 'Brown', 'Black', 'White', 'Pink']
menu = OptionMenu(App, menu_ch, *options)
menu_ch.set('Grey')
menu.config(width=20)
menu.grid(row=1, column=1, padx=70, pady=5)


def show():
    App['background'] = (menu_ch.get()).lower()


button = Button(App, text='Show', command=show)
button.grid(row=2, column=1, padx=70, pady=5)

App.mainloop()
