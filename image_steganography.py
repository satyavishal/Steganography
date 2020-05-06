# function converts the message to binary value
def msg_bin_conversion():
    msg=str(input("Enter your message here: \n"))
    #converts each character to the bin of its acsii value and joins it to the string.
    # The string is then split into a list
    msg_bin=(" ".join(f"{ord(i):08b}" for i in msg)).split(sep=" ")
    print(msg_bin)
msg_bin_conversion()
