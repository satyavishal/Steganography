msg=['01101000','01101001']
pix=[(33, 5, 45), (33, 5, 45), (34, 6, 46), (34, 6, 46), (34, 6, 46), (34, 6, 46), (33, 5, 45), (33, 5, 45), (33, 7, 46), (33, 7, 46), (33, 7, 46), (32, 6, 45), (32, 6, 45), (32, 6, 45), (31, 5, 44), (31, 5, 44), (32, 6, 45), (32, 6, 45), (32, 6, 45), (32, 6, 45)]
print(msg)
print(pix[0:6])
def encoder(bin_list, pixel_list):
    pos=0
    length=len(bin_list)

    # 1st loop iterates the 8 bit binaru elements in the bin_list
    for character in bin_list: #refers to each bit
        slice_min=0
        slice_max=3
        cg=list(pixel_list[pos])
        #print(cg)
        # loop is used to iterate a set of 3 pixels for 1 byte ie for each character
        for i in range(0,3): # refers to the pixel
            #print(character[slice_min:slice_max])
            cg=list(pixel_list[pos])
            cg_pos=0
            #print(cg, pos, i, slice_min,slice_max )
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
                    #print(character[slice_min:slice_max])
                    #print(bit)
                    if bit == '1':
                        if(cg[cg_pos]%2==0):
                            cg[cg_pos]-=1
                    else:
                        if(cg[cg_pos]%2 != 0):
                            cg[cg_pos]-=1
                    cg_pos+=1
                #cg_pos+=1

                if(cg[cg_pos]%2!=0 and (pos+1)//3 < length ):
                    cg[cg_pos]-=1
                elif(cg[cg_pos]%2 == 0 and (pos+1)//3 == length):
                    cg[cg_pos]-=1

                pixel_list[pos]=tuple(cg)
                pos+=1


            #print(i)

        #print(pos, character, length)
    #print(pos)

encoder(msg,pix)
print(pix[0:6])
