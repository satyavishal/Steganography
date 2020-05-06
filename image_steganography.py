from PIL import Image
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
def msg_bin_conversion():
    msg=str(input("Enter your message here: \n"))
    #converts each character to the bin of its acsii value and joins it to the string.
    # The string is then split into a list
    #msg_bin2=(" ".join(f"{ord(i):08b}" for i in msg)).split(sep=" ")
    msg_bin=[]
    for i in msg:
        msg_bin.append(decimal_bin_conversion(ord(i)))
    print(msg_bin)
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

#Takes the List of decimal equivalent of the characters of decoded Image and returns the message
def bin_msg_conversion(bin_value):
    msg_list=[]
    for i in bin_value:
        msg_list.append(chr(bin_decimal_conversion(i)))
    msg="".join(msg_list)
    print("converted : ",msg)

#Converts the modified pixel data into the  final Image
def pixel_img_conversion(pixel,im):
    img_out=Image.new(im.mode,im.size) #creating a new image object
    img_out.putdata(pixel)
    img_out.save('test_out.jpg')

#Extracts the pixel values from the given image file
def img_pixel_extraction(file_name):
    #im= Image.open('./testing_1.jpg')
    im=Image.open(file_name)
    pix_val = list(im.getdata())
    #print(pix_val)
    pixel_img_conversion(pix_val,im)
img_pixel_extraction('./testing_1.jpg')
