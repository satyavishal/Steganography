#pixel=[(32, 5, 45), (32, 5, 44), (34, 6, 46), (34, 5, 45), (34, 5, 46), (34, 5, 45),(33, 5, 45), (33, 5, 45), (34, 6, 46)]

# Decodes the msg from the given list of pixel data and returns the msg binary data
def decode(pix):
    msg_bin=[]
    pos=0
    while True:
        bin=[]
        flag=0
        for i in range(0,3):
            c=0
            for j in list(pix[pos]):
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
    #print(msg_bin)

#decode(pixel)
