from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk              # pip install pillow

App = Tk()
App.title('Change Icon Image')
App.geometry('500x500')

# Change the image icon of the display window
App.iconbitmap(r'Icons\Robot.ico')


# Display image in the application, with a file dialog box (directory for the image)
def img_select():
    # The 'img' variable made access-able out of this function
    global img

    # .fname --> store the location of the image file
    App.fname = filedialog.askopenfilename(initialdir='Icons', title='Select an image', filetypes=(
        ('PNG Images', '*.png'), ('ICON Files', '*.ico'), ('All Files', '*.*')))

    # Get rid of the button display after image is selected
    button.destroy()

    img = ImageTk.PhotoImage(Image.open(App.fname))
    lbl = Label(App, image=img)
    lbl.pack()


button = Button(App, text='View', command=img_select)
button.grid(padx=225, pady=100)

App.mainloop()
