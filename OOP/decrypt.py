# ask user for the input
input_string = input("What's the encrypted text you want to decrypt?:")
output_string = ""

# check the character using loop
for i in range(len(input_string)):
    # if *, change "a"
    if input_string[i] == "*":
        output_string += "a"
    # if &, change"e"
    elif input_string[i] == "&":
        output_string += "e"
    # if #, change "i"
    elif input_string[i] == "#":
        output_string += "i"
    # if +, change "o"
    elif input_string[i] == "+":
        output_string += "o"
    # if !, change "u"
    elif input_string[i] == "!":
        output_string += "u"
    else:
        output_string += input_string[i]
# print output
print("\nThe decrypted text is: ","\033[4m"+"\033[1;33m"+ output_string)
