from tkinter import *
from tkinter import filedialog

# Main Window
App = Tk()
App.title('Icon Creator')
App.geometry('300x200')


# Selecting the image from a file dialog box
def img_choose():
    from PIL import Image           # PIL --> Python Image Library
    global img

    App.img_dir = filedialog.askopenfilename(initialdir='C:', title='Choose an image',
                                             filetypes=(('PNG Icons', '*.png'),
                                                        ('JPG Icons', '*.jpg'),
                                                        ('All files', '*.*')))
    img = Image.open(App.img_dir)


# Convert image to .ico and save it
def img_convt():
    try:
        from PIL import Image

        # f'...' --> Formatted string
        # Saving the selected image as an Ico formatted file, and the given size (height x length)
        img.save(f'{icon_name.get()}.ico', format='ICO',
                 sizes=[(ico_size.get(), ico_size.get())])

        compl = Toplevel()
        compl.title('Success')
        compl.geometry('220x70')

        msg = Label(compl, text='Icon converted successfully!')
        msg.grid(row=4, column=1, columnspan=2, padx=35, pady=10)

        compl.mainloop()
    except:
        compl = Toplevel()
        compl.title('Failure')
        compl.geometry('220x70')

        msg = Label(compl, text="Something went wrong!")
        msg.grid(row=2, column=1, columnspan=2, padx=40, pady=10)

        compl.mainloop()


# Converted .ico preview
def preview():
    prev = Toplevel()
    prev.title('Icon Preview')
    prev.geometry('250x70')
    prev.iconbitmap(f'{icon_name.get()}.ico')

    lbl = Label(prev, text='Check your icon!')
    lbl.grid(row=2, column=1, columnspan=2, padx=75, pady=20)

    prev.mainloop()


# Choose label and button
pickL = Label(App, text='Select your image: ')
pickL.grid(row=0, column=0, pady=10)

pickB = Button(App, text='Choose', command=img_choose)
pickB.grid(row=0, column=1, pady=10)

# Icon size label and drop down menu
siz_lbl = Label(App, text='Select the icon size:')
siz_lbl.grid(row=1, column=0, pady=10)

ico_size = IntVar()
sizes = [16, 24, 32, 48, 64, 128, 255]
siz_menu = OptionMenu(App, ico_size, *sizes)
siz_menu.grid(row=1, column=1, pady=10)
ico_size.set(32)

# Icon name label and entry field
nam_lbl = Label(App, text='Enter the icon name: ')
nam_lbl.grid(row=2, column=0, pady=10)

icon_name = Entry(App)
icon_name.grid(row=2, column=1, pady=10)

# Convert button
conB = Button(App, text='Convert', command=img_convt)
conB.grid(row=3, column=0, pady=10)

# Preview button
prevB = Button(App, text='Preview', command=preview)
prevB.grid(row=3, column=1, pady=10)

App.mainloop()
