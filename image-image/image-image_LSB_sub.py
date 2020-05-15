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
3. The merged image is saved by default as .png, hence while saving file dont enter the extension.

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
    pix_val =im.load() #list(im.getdata())
    return pix_val,im

#Checing the size of the two images
def size_check(cover,secret):
    if (secret.size[0] > cover.size[0]) or (secret.size[1] > cover.size[1]):
        return True
    else:
        return False

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

#Merges the RBG values ie input is the rbg values of 2 pixles and output is the merged pixel rbg values
def merge_rbg(cov,sec):
    #Converting decimal RBG values into binary
    for i in range(3):
        cov[i]=decimal_bin_conversion(cov[i])
        sec[i]=decimal_bin_conversion(sec[i])

    r1,b1,g1=cov
    r2,b2,g2=sec
    #merging the rbg values
    merged_rbg_pix=[r1[:4]+r2[:4],
                    b1[:4]+b2[:4],
                    g1[:4]+g2[:4]]
    #Converting binary merged RBG values into decimal
    for i in range(3):
        merged_rbg_pix[i]=bin_decimal_conversion(merged_rbg_pix[i])

    return tuple(merged_rbg_pix)

#Merges the cover and secret images and saves the merged Image
def merge(cover_pix,cover_im,secret_pix,secret_im,img_name):
    #creating a new image object
    img_out=Image.new(cover_im.mode,cover_im.size)
    pixel_map=img_out.load()
    #Iterating through each pixel
    for i in range(cover_im.size[0]):
        for j in range(cover_im.size[1]):
            if i < secret_im.size[0] and j < secret_im.size[1]:
                pixel_map[i,j]=merge_rbg(list(cover_pix[i,j]),list(secret_pix[i,j]))
            else:
                pixel_map[i,j]=merge_rbg(list(cover_pix[i,j]),[0,0,0])
    #saving the merged image
    img_out.save(img_name)

#extracts the rbg values of the secret image
def extract_rbg(pix):
    #Converting decimal RBG values into binary
    for i in range(3):
        pix[i]=decimal_bin_conversion(pix[i])

    r,b,g=pix
    #Extracting the secret rbg values
    pix_out=[r[4:]+"0000",
             b[4:]+"0000",
             g[4:]+"0000"]

    #Converting binary Extracted RBG values into decimal
    for i in range(3):
        pix_out[i]=bin_decimal_conversion(pix_out[i])

    return tuple(pix_out)

#extracts the secret image pixel data and saves the image
def extract(merged_pix,merged_im,extract_name):
    #creating a new image object
    img_out=Image.new(merged_im.mode,merged_im.size)
    pixel_map_new=img_out.load()
    pix_size=merged_im.size

    #Iterating through each pixel
    for i in range(merged_im.size[0]):
        for j in range(merged_im.size[1]):
            pixel_map_new[i,j]=extract_rbg(list(merged_pix[i,j]))

            if pixel_map_new[i,j]!=(0,0,0):
                pix_size=(i+1,j+1)
    #cropping the image
    img_out=img_out.crop((0,0,pix_size[0],pix_size[1]))
    #saving the extracted Image
    img_out.save(extract_name)

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
        print("Select the 'Secret image' you want to hide after the 'dialog box' opens:")
        time.sleep(5)
        secret_img_name=select_img()
        #Checking for valid name
        if secret_img_name == "":
            print("please select an image!! retry again in 3sec")
            time.sleep(3)
            initializer(0)
        #getting the pixel data
        secret_pix_data,secret_im=img_pixel_extraction(secret_img_name)

        #selecting the cover image
        print("Note: Cover image size should be >= secret image size ")
        print("The secret image size you selected is: ",secret_im.size)
        print("Select the 'Cover image' you want the 'Secret image' to be hidden in after the 'dialog box' opens:")
        time.sleep(8)
        cover_img_name=select_img()
        #Checking for valid name
        if cover_img_name == "":
            print("please select an image!! retry again in 3sec")
            time.sleep(3)
            initializer(0)
        #getting the pixel data
        cover_pix_data,cover_im=img_pixel_extraction(cover_img_name)


        # Checking the image sizes and redirecting accordingly
        if size_check(cover_im,secret_im):
            print("Cover image is smaller than the Secret image")
            if int(input("Select '1' to retry and '0' to exit")) == 1:
                initializer(0)
            else:
                sys.exit()

        #saving the image
        print("Select the location and image name of the merged image without the extention:")
        time.sleep(5)
        save_img_name=save_img()
        #Checking for valid name
        if save_img_name == "":
            print("please enter the name and location for the extracted image!! retry again in 3sec")
            time.sleep(3)
            initializer(0)

        #Merging the images
        merge(cover_pix_data,cover_im,secret_pix_data,secret_im,save_img_name)

    #Extracting the secret image
    elif choice == '0':
        #Selecting the stego object
        print("Select the image you want to Decode to extract the secret image after the 'dialog box' opens")
        time.sleep(5)
        merged_img_name=select_img()
        if merged_img_name == "":
            print("please select an image, retry again in 3sec")
            time.sleep(3)
            initializer(0)

        #Selecting the save location of the extracted secret Image
        print("Select the save location of the extracted image after the 'dialog box' opens")
        time.sleep(5)
        extract_name=save_img()
        if extract_name == "":
            print("please select an image!! retry again in 3sec")
            time.sleep(3)
            initializer(0)

        merged_pix,merged_im= img_pixel_extraction(merged_img_name)

        exract_pix=extract(merged_pix,merged_im,extract_name)

        pixel_img_conversion(extract_name,exract_pix,merged_im)

    #Exit
    elif choice == '5':
        exit()

    #Invalid entry
    else:
        print("Invalid entry pls try again is 3sec")
        time.sleep(3)
        initializer(0)

initializer(1)
