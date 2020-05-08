pixel=[(31, 5, 44), (32, 6, 45), (32, 6, 45), (33, 7, 46), (33, 7, 46), (32, 6, 45), (32, 6, 45), (31, 5, 44), (32, 6, 45), (32, 6, 45), (32, 6, 45), (32, 6, 45), (32, 6, 45), (32, 6, 45), (32, 6, 45), (32, 6, 45), (31, 6, 45), (31, 6, 45), (31, 6, 45)]


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


# Decodes the msg from the given list of pixel data and returns the msg binary data
def decode(pix):
    #pix=pixel[0]
    msg_bin=[]
    pos=0
    while True:
        bin=[]
        flag=0
        for i in range(0,3):
            print(pos)
            c=0
            z=list(pix[pos])
            for j in z:
                c+=1
                if(i==2 and c==3 ):
                    #print(j)
                    if (j%2!=0):
                        flag=1
                        break
                else:
                    if(j%2 == 0):
                        #print(j)
                        bin.append('0')
                    else:
                        bin.append('1')

            pos+=1
            if(flag==1):
                break

        msg_bin.append("".join(bin))
        if(flag==1):
            break
    #return msg_bin
    #print(msg_bin)
    bin_msg_conversion(msg_bin)

decode(pixel)
