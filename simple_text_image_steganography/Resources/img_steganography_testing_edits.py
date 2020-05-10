from PIL import Image
from os import system,name
#from decode import *
#from encode import *
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
    msg_bin=[]
    for i in msg:
        msg_bin.append(decimal_bin_conversion(ord(i)))
    return msg_bin

#Encodes the given binary data to the pixel data.Modifies the list as list is
#passed by using call by reference ie It does'nt return anything.
def encoder(bin_list, pixel_list):
    pos=0
    length=len(bin_list)

    # 1st loop iterates the 8 bit binaru elements in the bin_list
    for character in bin_list: #refers to each bit
        slice_min=0
        slice_max=3
        cg=list(pixel_list[pos])

        # loop is used to iterate a set of 3 pixels for 1 byte ie for each character
        for i in range(0,3): # refers to the pixel
            cg=list(pixel_list[pos])
            cg_pos=0

            # this block is executed for 1st 3 pixel packets in the set
            if i!=2:
                for bit in character[slice_min:slice_max]:
                    #print(character[slice_min:slice_max])
                    if bit == '1':
                        if(cg[cg_pos]%2==0):
                            cg[cg_pos]-=1
                    else:
                        if(cg[cg_pos]%2 != 0):
                            cg[cg_pos]-=1
                    cg_pos+=1
                pixel_list[pos]=tuple(cg)
                slice_min+=3
                if i == 1:
                    slice_max+=2
                else:
                    slice_max+=3
                pos+=1

            # this block is executed for the last pixel packet in the set
            elif(i == 2):
                for bit in character[slice_min:slice_max]:
                    if bit == '1':
                        if(cg[cg_pos]%2==0):
                            cg[cg_pos]-=1
                    else:
                        if(cg[cg_pos]%2 != 0):
                            cg[cg_pos]-=1
                    cg_pos+=1

                if(cg[cg_pos]%2!=0 and (pos+1)//3 < length ):
                    cg[cg_pos]-=1
                elif(cg[cg_pos]%2 == 0 and (pos+1)//3 == length):
                    cg[cg_pos]-=1

                pixel_list[pos]=tuple(cg)
                pos+=1

# Decodes the msg from the given list of pixel data and returns the msg binary data
def decode(pix):
    #pix=pixel[0]
    msg_bin=[]
    pos=0
    while True:
        bin=[]
        flag=0
        for i in range(0,3):
            c=0
            z=list(pix[pos])
            for j in z:
                c+=1
                if(i==2 and c==3 ):
                    if (j%2!=0):
                        flag=1
                        break
                else:
                    if(j%2 == 0):
                        bin.append('0')
                    else:
                        bin.append('1')
            pos+=1
            if(flag==1):
                break
        msg_bin.append("".join(bin))
        if(flag==1):
            break
    return msg_bin

#Encodes the given binary data to the pixel data.Modifies the list as list is
#passed by using call by reference ie It does'nt return anything.
def encoder(bin_list, pixel_list):
    pos=0
    length=len(bin_list)

    # 1st loop iterates the 8 bit binaru elements in the bin_list
    for character in bin_list: #refers to each bit
        slice_min=0
        slice_max=3
        cg=list(pixel_list[pos])

        # loop is used to iterate a set of 3 pixels for 1 byte ie for each character
        for i in range(0,3): # refers to the pixel
            cg=list(pixel_list[pos])
            cg_pos=0

            # this block is executed for 1st 3 pixel packets in the set
            if i!=2:
                for bit in character[slice_min:slice_max]:
                    #print(character[slice_min:slice_max])
                    if bit == '1':
                        if(cg[cg_pos]%2==0):
                            cg[cg_pos]-=1
                    else:
                        if(cg[cg_pos]%2 != 0):
                            cg[cg_pos]-=1
                    cg_pos+=1
                pixel_list[pos]=tuple(cg)
                slice_min+=3
                if i == 1:
                    slice_max+=2
                else:
                    slice_max+=3
                pos+=1

            # this block is executed for the last pixel packet in the set
            elif(i == 2):
                for bit in character[slice_min:slice_max]:
                    if bit == '1':
                        if(cg[cg_pos]%2==0):
                            cg[cg_pos]-=1
                    else:
                        if(cg[cg_pos]%2 != 0):
                            cg[cg_pos]-=1
                    cg_pos+=1

                if(cg[cg_pos]%2!=0 and (pos+1)//3 < length ):
                    cg[cg_pos]-=1
                elif(cg[cg_pos]%2 == 0 and (pos+1)//3 == length):
                    cg[cg_pos]-=1

                pixel_list[pos]=tuple(cg)
                pos+=1

# Decodes the msg from the given list of pixel data and returns the msg binary data
def decode(pix):
    #pix=pixel[0]
    msg_bin=[]
    pos=0
    while True:
        bin=[]
        flag=0
        for i in range(0,3):
            c=0
            z=list(pix[pos])
            for j in z:
                c+=1
                if(i==2 and c==3 ):
                    if (j%2!=0):
                        flag=1
                        break
                else:
                    if(j%2 == 0):
                        bin.append('0')
                    else:
                        bin.append('1')
            pos+=1
            if(flag==1):
                break
        msg_bin.append("".join(bin))
        if(flag==1):
            break
    return msg_bin

#Takes 8 bit binary as input and returns the decimal equivalent which is the ACSII value
def bin_decimal_conversion(x):
    c=7
    decimal=0
    for i in x:
        decimal=decimal+(int(i)*(2**c))
        c-=1
    return decimal

#Takes the List of binary equivalent of the characters of
#decoded Image and prints the message on the console
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
    im=Image.open(file_name)
    pix_val = list(im.getdata())
    return pix_val,im

#This controls the whole programs execution flow
def initializer():
    clear()
    choice=input("Simple Image Steganography\nEnter:\n '1' to Encode the image\n '0' to Decode the image\n '5' to exit\n")

    #Encoding the image
    if choice == '1':
        msg=str(input("Enter the message you want to encode: \n"))
        img_name=str(input("Enter the name of the image with the extention: "))
        img_out_name=str(input("Enter the name of the encoded image with the extention: "))
        msg_bin_list=msg_bin_conversion(msg)
        img_pixel_list,im= img_pixel_extraction(img_name)
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

    #Decoding the image
    elif choice == '0':
        img_name=str(input("Enter the name of the image without the extention: "))
        img_pixel_list,im= img_pixel_extraction(img_name)
        #f = open( 'file3.py', 'w' )
        #f.write(str(img_pixel_tuple))
        #f.close()
        #img_pixel_list=list(img_pixel_tuple)
        #decode(img_pixel_list)
        #f = open( 'file.py', 'w' )
        #f.write(str(img_pixel_list))
        #f.close()
        #print(type(img_pixel_tuple))
        #print(type(img_pixel_list))
        #print(img_pixel_list[0:20])
        msg_bin=decode(img_pixel_list)
        bin_msg_conversion(msg_bin)

    #Exit
    elif choice == '5':
        exit()

    #Invalid entry
    else:
        print("Invalid entry pls try again is 3sec")
        time.sleep(3)
        initializer()

initializer()
