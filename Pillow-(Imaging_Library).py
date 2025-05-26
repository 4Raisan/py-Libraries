'''The Python Imaging Library (Pillow or PIL) supports a wide range of image formats for opening, saving, and converting images.'''

# 1. Use with Tkinter for display in the GUI
from tkinter import *
from PIL import ImageTk,Image

img = ImageTk.PhotoImage(Image.open(Part-07-(sample_1).jpg))  # make Object for image
labelimg = Label(image=img)  # make Label for image
labelimg.grid(row=0, column=0)  # display image

root.mainloop()

