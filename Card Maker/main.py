from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import glob

# Outline the basic structure
root = Tk()
root.title("Exceed Builder")
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=N+E+S+W)

# TODO: Clean this up
for row_index in range(3):
    Grid.rowconfigure(mainframe, row_index, weight=1)
    for col_index in range(3):
        Grid.columnconfigure(mainframe, col_index, weight=1)

style = ttk.Style()
style.configure("blackbox.TFrame", foreground='black', background='black')

elements_frame = ttk.Frame(mainframe, style='blackbox.TFrame').grid(column=0, row=0, sticky=N+E+S+W)
canvas_frame = ttk.Frame(mainframe).grid(column=1, row=0, sticky=N+E+S+W)
stats_frame = ttk.Frame(mainframe).grid(column=2, row=0, sticky=N+E+S+W)


ttk.Label(elements_frame, text="test")

# img = ImageTk.PhotoImage(Image.open("Templates\Default\Stat Blocks\Armor.png"))

# label = tkinter.Label(image=img)
# label.image = img

# label.place(x=0, y=0)
root.mainloop()