from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import glob

# Sorry for this, but I have no idea how to create a GUI properly, so I'm fumbling around here.
# If the code seems disorganized, that's because it is.

def collapse(frame, col_index):
    Grid.columnconfigure(frame, col_index, weight=0)

def expand(frame, col_index):
    Grid.columnconfigure(frame, col_index, weight=1)

# Create and set up the root window.
root = Tk()
root.title("Exceed Builder")
root.geometry("852x480")

# Set up the grid
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)

# Set up the main frame, which is the frame that contains everything else.
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=N+E+S+W)

# Set up main grid
Grid.rowconfigure(mainframe, 0)
Grid.rowconfigure(mainframe, 1, weight=1)
for col_index in range(3):
    Grid.columnconfigure(mainframe, col_index, weight=1)
Grid.columnconfigure(mainframe, 1, weight=2)

# Set up all the styles we'll be using.
style = ttk.Style()
style.configure("elements.TFrame", background='grey')
style.configure("stats.TFrame", background='grey')
style.configure("menu_bar.TFrame", background='grey')
style.configure("menu.TButton")

# Set up frames for each segment of the GUI
menu_bar = ttk.Frame(mainframe, style='menu_bar.TFrame')
menu_bar.grid(column=0, row=0, columnspan=3, sticky=NW)
for col_index in range(5):
    Grid.columnconfigure(menu_bar, col_index)

elements_frame = ttk.Frame(mainframe, style='elements.TFrame')
elements_frame.grid(column=0, row=1, rowspan=3, sticky=N+E+S+W)

canvas_frame = ttk.Frame(mainframe)
canvas_frame.grid(column=1, row=1, rowspan=3, sticky=N+E+S+W)

stats_frame = ttk.Frame(mainframe, style="stats.TFrame")
stats_frame.grid(column=2, row=1, rowspan=3, sticky=N+E+S+W)

# Set up the menu bar, which allows the user to complete various application-level actions, like saving or loading.
menu_bar_button_padding = "15 4 10 4"
ttk.Button(menu_bar, text="File", width=4, style="Toolbutton", padding=menu_bar_button_padding).grid(column=0, row=0, sticky=NW)
ttk.Button(menu_bar, text="Edit", width=4, style="Toolbutton", padding=menu_bar_button_padding).grid(column=1, row=0, sticky=NW)

#ttk.Label(elements_frame, text="test").grid(column=1, row=0, sticky=N)

# img = ImageTk.PhotoImage(Image.open("Templates\Default\Stat Blocks\Armor.png"))

# label = tkinter.Label(image=img)
# label.image = img

# label.place(x=0, y=0)
root.mainloop()