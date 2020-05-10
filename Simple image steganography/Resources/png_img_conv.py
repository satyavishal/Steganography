from PIL import Image

#Converts the modified pixel data into the  final Image
def pixel_img_conversion(img_name,pixel,im):
    img_out=Image.new(im.mode,im.size) #creating a new image object
    img_out.putdata(pixel)
    img_out.save(img_name)

#Extracts the pixel values from the given image file
def img_pixel_extraction(file_name):
    #extracting jpg img pixel data
    im=Image.open(file_name)
    pix_val = list(im.getdata())
    print(pix_val)
    if len(pix_val[0])==4:
        rbga_img=Image.open(file_name)
        rbga_img.load()
        new_im=Image.new("RGB",rbga_img.size,(255,255,255))
        new_im.paste(rbga_img, mask=rbga_img.split()[3])
        new_im.save("sample_2.jpg", "JPEG", quality=100)
        im2=Image.open(".\conv_dump\sam.jpg")
        pix_val2 = list(im2.getdata())
        return pix_val2,im2
    else:
        return pix_val,im
img_pixel_extraction("test_rbga.png")
