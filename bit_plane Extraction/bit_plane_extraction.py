from PIL import Image
from os import system,name
import time
import tkinter as tk
from tkinter import filedialog
import os
import multiprocessing as mp

#opens a dialog box to select an image
def select_img():
    root=tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="S:\\Projects",title="Select an image",
    filetypes=(("all files","*.*"),("jpg files","*.jpg"),("png files","*.png")))
    return file_path

#opens a dialog box to save a file
def Save_file():
    root=tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Save the image",
    defaultextension=".png",initialdir="S:\\Projects")
    return file_path

#opens a new image object takes file name as the input
def image_pixel(file_name):
    im=Image.open(file_name)
    pix_list=list(im.getdata())
    return pix_list,im

# creates an empty image object takes pixels list ,new file name,original im object as input
def pixel_image(fileout,pixels,im):
    img_out=Image.new(im.mode,im.size)
    img_out.putdata(pixels)
    img_out.save(fileout)

#takes decimal number as the input and retunrs its binary equivalent
def decimal_bin_conversion(x):
    l=[]
    while (x!=0) :
        l.append(str(x % 2))
        x=int(x/2)
    ln=len(l)
    if(ln!=8):
        for i in range(0,(8-ln)):
            l.append(str(0))
    l.reverse()
    return "".join(l)

#takes a pixel list and modifies it as a list of rbg values in binary
def pixel_bin_conversion(pixels):
    l=[]
    for i in pixels:
        for j in i:
            l.append(decimal_bin_conversion(j))
    return l

#takes binary number as input and returns its equivalent decimal value
def bin_decimal_conversion(x):
    c=7
    decimal=0
    for i in x:
        decimal=decimal+(int(i)*(2**c))
        c-=1
    return decimal

#takes a binary list and modifies it as a list of tuples of rbg values
def bin_pixel_conversion(pixels):
    c=0
    for i in pixels:
        l=[]
        for j in i:
            l.append(bin_decimal_conversion(j))
        pixels[c]=tuple(l)
        c+=1

def bit_plane_extraction(pixels,pos,im):
    plane=[]
    for i in pixels:
        plane.append(i[pos]+"0000000")
    plane_iter=iter(plane)
    final=list(zip(plane_iter,plane_iter,plane_iter))
    bin_pixel_conversion(final)
    pixel_image("plane{num}.png".format(num=pos),final,im)
    #print(plane)


def initializer(num):
    print("select the image you wanna extract the bit plane for after the dialog box appears:")
    file_name=select_img()
    pix,im=image_pixel(file_name)
    l=pixel_bin_conversion(pix)
    #pool = mp.Pool(mp.cpu_count())
    #for i in range (7,-1,-1):
    #    pool.apply_async(bit_plane_extraction, args=(pix,i))
    bit_plane_extraction(l,0,im)

initializer(0)
