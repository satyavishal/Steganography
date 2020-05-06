# function converts the message to binary value list
def msg_bin_conversion():
    msg=str(input("Enter your message here: \n"))
    #converts each character to the bin of its acsii value and joins it to the string.
    # The string is then split into a list
    msg_bin=(" ".join(f"{ord(i):08b}" for i in msg)).split(sep=" ")
    print(msg_bin)
    bin_msg_conversion(msg_bin)
#msg_bin_conversion()

def bin_decimal_conversion(x):
    c=7
    decimal=0
    for i in x:
        decimal=decimal+(int(i)*(2**c))
        c-=1
    return decimal

def bin_msg_conversion(bin_value):
    msg_list=[]
    for i in bin_value:
        msg_list.append(chr(bin_decimal_conversion(i)))
    msg="".join(msg_list)
    print("converted : ",msg)

msg_bin_conversion()
