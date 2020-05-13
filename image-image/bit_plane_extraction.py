from PIL import Image
from os import system,name
import time
import tkinter as tk
from tkinter import filedialog
import os

#opens a new image object takes file name as the input
def image-pixel(file_name):
    im=Image.new(file_name)
    pix_list=list(im.getdata())
    return pix_list,im

# creates an empty image object takes pixels list ,new file name,original im object as input
def pixel-image(fileout,pixels,im):
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

#takes a pixel list and modifies it as a list of lists of rbg values in binary
def pixel_bin_conversion(pixels):
    c=0
    for i in pixels:
        l=[]
        for j in i:
            l.append(decimal_bin_conversion(j))
        pixels[c]=l
        c+=1

#takes binary number as input and returns its equivalent decimal value
def bin_decimal_conversion(x):
    c=7
    decimal=0
    for i in x:
        decimal=decimal+(int(i)*(2**c))
        c-=1
    return decimal

def bin_pixel_conversion(pixels):
    c=0
    for i in pixels:
        l=[]
        for j in i:
            l.append(bin_decimal_conversion(j))
        pixels[c]=tuple(l)
        c+=1


def bit_plane_extraction(pixels):
