from PIL import Image
from os import system,name
from decode import *
from encode import *
import time

#Clears the console screen
def clear():
    #For windows
    if name=='nt':
        _=system('cls')
    #For mac os and linux
    else:
        _=system('clear')

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

# function converts the message to binary value list
def msg_bin_conversion(msg):
    #msg=str(input("Enter your message here: \n"))
    #converts each character to the bin of its acsii value and joins it to the string.
    # The string is then split into a list
    #msg_bin2=(" ".join(f"{ord(i):08b}" for i in msg)).split(sep=" ")
    msg_bin=[]
    for i in msg:
        msg_bin.append(decimal_bin_conversion(ord(i)))
    return msg_bin
    #print(msg_bin)
    #print(msg_bin2)
    #bin_msg_conversion(msg_bin)

#Takes 8 bit binary as input and returns the decimal equivalent which is the ACSII value
def bin_decimal_conversion(x):
    c=7
    decimal=0
    for i in x:
        decimal=decimal+(int(i)*(2**c))
        c-=1
    return decimal

#Takes the List of binary equivalent of the characters of decoded Image and returns the message
def bin_msg_conversion(bin_value):
    msg_list=[]
    for i in bin_value:
        msg_list.append(chr(bin_decimal_conversion(i)))
    msg="".join(msg_list)
    print("Decoded message:\n ",msg)

#Converts the modified pixel data into the  final Image
def pixel_img_conversion(img_name,pixel,im):
    img_out=Image.new(im.mode,im.size) #creating a new image object
    img_out.putdata(pixel)
    img_out.save(img_name)

#Extracts the pixel values from the given image file
def img_pixel_extraction(file_name):
    #im= Image.open('./testing_1.jpg')
    im=Image.open(file_name)
    pix_val = list(im.getdata())
    #print(pix_val)
    #pixel_img_conversion(pix_val,im)
    return pix_val,im
#img_pixel_extraction('./testing_1.jpg')

#This controls the whole programs execution flow
def initializer():
    clear()
    choice=input("Enter:\n '1' to Encode the image\n '0' to Decode the image\n '5' to exit\n")
    if choice == '1':
        msg=str(input("Enter the message you want to encode: \n"))
        img_name=str(input("Enter the name of the image with the extention: "))
        img_out_name=str(input("Enter the name of the encoded image with the extention: "))
        msg_bin_list=msg_bin_conversion(msg)
        img_pixel_list,im= img_pixel_extraction(img_name)
        #print(img_pixel_list)
        img_pixel_list_out=img_pixel_list.copy()
        encoder(msg_bin_list,img_pixel_list_out)
        pixel_img_conversion(img_out_name, img_pixel_list_out, im)
        #f = open( 'file_encoded_data.py', 'w' )
        #f.write(str(img_pixel_list_out))
        #f.close()
        """print(msg_bin_list[0])
        print(img_pixel_list[0:3])
        print(img_pixel_list_out[0:3])
        print(msg_bin_list[1])
        print(img_pixel_list[3:6])
        print(img_pixel_list_out[3:6])"""

    elif choice == '0':
        """decoder code"""
        img_name=str(input("Enter the name of the image with the extention: "))
        img_pixel_list,im= img_pixel_extraction(img_name)
        #f = open( 'file3.py', 'w' )
        #f.write(str(img_pixel_tuple))
        #f.close()
        #img_pixel_list=list(img_pixel_tuple)
        #decode(img_pixel_list)
        f = open( 'file.py', 'w' )
        f.write(str(img_pixel_list))
        f.close()
        #print(type(img_pixel_tuple))
        #print(type(img_pixel_list))
        #print(img_pixel_list[0:20])
        msg_bin=decode(img_pixel_list)
        bin_msg_conversion(msg_bin)
    elif choice == '5':
        exit()
    else:
        print("Invalid entry pls try again is 3sec")
        time.sleep(3)
        initializer()

initializer()
