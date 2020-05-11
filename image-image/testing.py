from PIL import Image
from os import system,name
import time
import tkinter as tk
from tkinter import filedialog
import os

def img_pixel_extraction(file_name):
    im=Image.open(file_name)
    print(im.size[0])

img_pixel_extraction(".\\images\\cover_img(1920X1200).jpg")
