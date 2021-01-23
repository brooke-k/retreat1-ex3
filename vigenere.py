<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
#vigenere.py

# Decode a Vigenère cipher on the message
def decode_vigenere(message, secret):
    newmsg = ""
    for i in range(len(message)):
        if(message[i].isupper()):
            number = 65 + (ord(message[i]) - ord(secret[i%len(secret)])) % 26
            newmsg += chr(number)
        elif(message[i].islower()):
            number = 97 + (ord(message[i]) - ord(secret[i%len(secret)])) % 26
            newmsg += chr(number) 
        else:
            newmsg += message[i]
    return newmsg

<<<<<<< HEAD
=======
#vigenere.py

>>>>>>> 4519d86... Encode Part 1
=======
#vigenere.py

>>>>>>> 4519d86... Encode Part 1
=======
>>>>>>> 029927e... Decode Vigenere and Add Art
# Performs the Vigenère cipher operation
def encode_vigenere(message, secret):
    newmsg = ""
    for i in range(len(message)):
        if(message[i].isupper()):
            number = 65 + (ord(message[i]) + ord(secret[i%len(secret)]) - 2*65) % 26
            newmsg += chr(number)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    return newmsg
>>>>>>> 029927e... Decode Vigenere and Add Art
=======
    return newmsg
>>>>>>> 4519d86... Encode Part 1
=======
=======
        elif(message[i].islower()):
            number = 97 + (ord(message[i]) + ord(secret[i%len(secret)]) - 2*97) % 26
            newmsg += chr(number)
>>>>>>> c2a7fe8... Encode Part 3
=======
        elif(message[i].islower()):
            number = 97 + (ord(message[i]) + ord(secret[i%len(secret)]) - 2*97) % 26
            newmsg += chr(number)
>>>>>>> c2a7fe8... Encode Part 3
        else:
            newmsg += message[i]
    return newmsg
>>>>>>> cce050d... Encode Part 2
=======
    return newmsg
>>>>>>> 4519d86... Encode Part 1
