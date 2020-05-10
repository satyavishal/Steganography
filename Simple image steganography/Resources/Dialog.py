import tkinter as tk
from tkinter import filedialog

#opens a dialog box to select an image
def select_img():
    root=tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="C:",title="Select an image",
    filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    return file_path

#opens a dialog box to save a file
def Save_file():
    root=tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Save the image",
    defaultextension=".png",initialdir="C:")
    return file_path

Save_file()
