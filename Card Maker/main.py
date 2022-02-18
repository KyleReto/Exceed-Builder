from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import ImageTk,Image
import glob

# Sorry for this, but I have no idea how to create a GUI properly, so I'm fumbling around here.
# If the code seems disorganized, that's because it is.

is_elements_collapsed = False
def toggle_elements():
    global is_elements_collapsed
    if is_elements_collapsed:
        Grid.grid(elements_frame)
        collapse_elements_button.text = '<<'
        is_elements_collapsed = False
    else:
        Grid.grid_remove(elements_frame)
        collapse_elements_button.text = '>>'
        is_elements_collapsed = True

is_stats_collapsed = False
def toggle_stats():
    global is_stats_collapsed
    if is_stats_collapsed:
        Grid.grid(stats_frame)
        collapse_stats_button.text = '<<'
        is_stats_collapsed = False
    else:
        Grid.grid_remove(stats_frame)
        collapse_stats_button.text = '>>'
        is_stats_collapsed = True

# Create and set up the root window.
root = Tk()
root.title("Exceed Builder")
root.geometry("852x480")

# Set up all the styles we'll be using.
style = ttk.Style()
style.configure("mainframe.TFrame", background='grey')
style.configure("elements_frame.TFrame", background='grey')
style.configure("canvas_frame.TFrame", background='white')
style.configure("stats_frame.TFrame", background='grey')
style.configure("menu_bar.TFrame", background='grey')

style.configure("Toolbutton", background='grey')

# Set up the grid
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)

# Set up the main frame, which is the frame that contains everything else.
mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=N+E+S+W)

# Set up main grid
Grid.rowconfigure(mainframe, 0)
Grid.rowconfigure(mainframe, 1, weight=1)
for col_index in range(3):
    Grid.columnconfigure(mainframe, col_index, weight=1)
Grid.columnconfigure(mainframe, 1, weight=2)

# Set up frames for each segment of the GUI
menu_bar = ttk.Frame(mainframe, style='menu_bar.TFrame')
menu_bar.grid(column=0, row=0, columnspan=3, sticky=NW)
for col_index in range(5):
    Grid.columnconfigure(menu_bar, col_index)
elements_frame = ttk.Frame(mainframe, style='elements_frame.TFrame')
elements_frame.grid(column=0, row=1, rowspan=3, sticky=N+E+S+W)
canvas_frame = ttk.Frame(mainframe)
canvas_frame.grid(column=1, row=1, rowspan=3, sticky=N+E+S+W)
stats_frame = ttk.Frame(mainframe, style="stats_frame.TFrame")
stats_frame.grid(column=2, row=1, rowspan=3, sticky=N+E+S+W)

# Set up the menu bar, which allows the user to complete various application-level actions, like saving or loading.
menu_bar_button_padding = "15 4 10 4"
ttk.Button(menu_bar, text="File", width=4, style="Toolbutton", padding=menu_bar_button_padding).grid(column=0, row=0, sticky=NW)
ttk.Button(menu_bar, text="Edit", width=4, style="Toolbutton", padding=menu_bar_button_padding).grid(column=1, row=0, sticky=NW)

# Set up the elements frame, which allows the user to add elements to the canvas.
collapse_elements_button = ttk.Button(elements_frame, text='<<', command=toggle_elements)
collapse_elements_button.grid(column=0, row=0, sticky=NE)

# Set up the stats frame, which allows the user to adjust the stats of the card on the canvas.
collapse_stats_button = ttk.Button(stats_frame, text='<<', command=toggle_stats)
collapse_stats_button.grid(column=0, row=0, sticky=NE)

# img = ImageTk.PhotoImage(Image.open("Templates\Default\Stat Blocks\Armor.png"))

# label = tkinter.Label(image=img)
# label.image = img

# label.place(x=0, y=0)
root.mainloop()