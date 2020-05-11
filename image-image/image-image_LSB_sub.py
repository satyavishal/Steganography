from PIL import Image
from os import system,name
import time
import tkinter as tk
from tkinter import filedialog
import os
"""
cover_img_names=["cover_img(1920X1200).jpg","cover_img(1920X1200).png",]

secret_img_names=["secret_img-1(512X288).jpg","secret_img-2(1920x1080).jpg","secret_img-3(1920x1080).jpg","secret_img(540X960).jpg",
                 "secret_img(640X960).png","secret_img-1(1920x1200).jpg","secret_img-2(1920x1200).jpg","secret_img-3(1920x1200).png"]
"""
info="""Steganography is the practice of concealing a file, message, image or video within
another file, message, image, or video.

In this project I am concealing a secret image in a cover image, ie Image in an Image Stegenography

Note:
1. Cover image Dimensions(Size) should be larger than or atleast equal to the secret image.
2. Always save the merged image in PNG format to avoid compression of the image.
   Also when sending the image over the internet make sure there is no compression, to do soo you can zip
   the image or convert it into rar and send it, or send the image as document if you are sending it via watsapp.
3. The merged image is saved by default as .png, hence while saving file dont enter the extension

"""


#Clears the console screen
def clear():
    #For windows
    if name=='nt':
        _=system('cls')
    #For mac os and linux
    else:
        _=system('clear')

#opens a dialog box to select an image
def select_img():
    root=tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir="S:\\Projects",title="Select an image",
    filetypes=(("all files","*.*"),("jpg files","*.jpg"),("png files","*.png")))
    return file_path

#opens a dialog box to save a file
def save_img():
    root=tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Save the image",
    defaultextension=".png",initialdir="S:\\Projects")
    return file_path

#Extracts the pixel values from the given image file
def img_pixel_extraction(file_name):
    im=Image.open(file_name)
    pix_val =list(im.getdata())
    print(pix_val)
    return pix_val,im

#Converts the modified pixel data into the  final Image
def pixel_img_conversion(img_name,pixel,im):
    img_out=Image.new(im.mode,im.size) #creating a new image object
    img_out.putdata(pixel)
    img_out.save(img_name+".png")

#Checing the size of the two images
def size_check(cover,secret):
    if (secret.size[0] > cover.size[0]) or (secret.size[1] > cover.size[1]):
        return False
    else:
        return True

#Takes integer as input and returns an 8bit binary value
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

#Takes 8 bit binary as input and returns the decimal equivalent which is the ACSII value
def bin_decimal_conversion(x):
    c=7
    decimal=0
    for i in x:
        decimal=decimal+(int(i)*(2**c))
        c-=1
    return decimal

#This controls the whole programs execution flow
def initializer(num):
    if num==0:
        clear()
    else:
        print(info)
        choice=input("Image in Image Steganography\nEnter:\n '1' to merge the images\n '0' to extract the secret image\n '5' to exit\n")

    #Merging the images
    if choice == '1':
        #selecting the secret image
        print("Note: Cover image is the image ")
        print("Select the 'Secret image' you want to hide after the 'dialog box' opens:")
        time.sleep(5)
        secret_img_name=select_img()

        #selecting the cover image
        print("Select the 'Cover image' you want the 'Secret image' to be hidden in after the 'dialog box' opens:")
        time.sleep(5)
        cover_img_name=select_img()

        #saving the image
        print("Select the location and image name of the merged image without the extention:")
        time.sleep(5)
        save_img_name=save_img()

        #getting the pixel data
        cover_pix_data,cover_im=img_pixel_extraction(cover_img_name)
        secret_pix_data,secret_im=img_pixel_extraction(secret_img_name)

        # Checking the image sizes and redirecting accordingly
        if !size_check(cover_im,secret_im):
            print("Cover image is smaller than the Secret image")
            if int(input("Select '1' to retry and '0' to exit")) == 1:
                initializer(0)
            else:
                sys.exit()

        #Merging the images
        merged_pix=merge(cover_img_name,secret_img_name)

        #saving the merged image
        pixel_img_conversion(save_img_name,merged_pix,cover_im)

    #Decoding the image
    elif choice == '0':
        print("Select the image you want to Decode to extract the secret image after the 'dialog box' opens")
        time.sleep(5)
        merged_img_name=select_img()

        print("Select the save location of the extracted image after the 'dialog box' opens")
        time.sleep(5)
        extract_name=select_img()

        merged_pix,merged_im= img_pixel_extraction(img_name)

        exract_pix=extract(img_pixel_list)
        pixel_img_conversion(extract_name,exract_pix,merged_im)

    #Exit
    elif choice == '5':
        sys.exit()

    #Invalid entry
    else:
        print("Invalid entry pls try again is 3sec")
        time.sleep(3)
        initializer()


print(info)
#initializer(1)
