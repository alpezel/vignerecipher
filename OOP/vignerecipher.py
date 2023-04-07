# ask the user for input message and key
message=input("MESSAGE (input in uppercase letters, no spaces): ")
key=input("KEYWORD (input in uppercase letters, no spaces): ")
# convert message and key to lists of numbers 0-25 since A-Z is in 65-90
message_num = [ord(c) - 65 for c in message]
key_num = [ord(c) - 65 for c in key]
# repeating the key until its the same length of the message
key_rep = []
key_index = 0
for i in range(len(message)):
    key_rep.append(key_num[key_index])
    key_index = (key_index + 1) % len(key)
# encrypt by adding message and key_rep, take the result mod 26
ciphertext_num = []
for i in range(len(message)):
    mn = message_num[i]
    kr = key_rep[i]
    ciphertext_num.append((mn + kr) % 26)
# convert ciphertext numbers to letters
ciphertext = ''
for c in ciphertext_num:
    ciphertext += chr(c + 65)
# print the output
print("\n","\033[4m"+"\033[1;36m"+ciphertext)