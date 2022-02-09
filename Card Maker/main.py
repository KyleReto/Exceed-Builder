from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image
import glob

root = Tk()

template = StringVar(root)
template.set("one")

template_menu = OptionMenu(root, template, "one", "two", "three")
template_menu.pack()

# img = ImageTk.PhotoImage(Image.open("Templates\Default\Stat Blocks\Armor.png"))

# label = tkinter.Label(image=img)
# label.image = img

# label.place(x=0, y=0)
root.mainloop()