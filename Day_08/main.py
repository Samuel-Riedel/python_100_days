alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
start = True

def caesar(text,shift,direction):
    encoded_word = []
    for i in text:
        index_text = alphabet.index(i)
        if direction == "encode":
            index_text += shift 
            encoded_word.append(alphabet[index_text])
            #print(f"The encoded message is: {alphabet[index_text]}")
        if direction == "decode":
            index_text -= shift 
            encoded_word.append(alphabet[index_text])
            #print(f"The encoded message is: {alphabet[index_text]}")
    print("".join(encoded_word))
    


def programExe():

    continueExe = input("Do you want to run the program again? Type Yes or No").lower()

    if continueExe == "no":
            start == False
            
    if continueExe == "yes":
            start == True
            text = input("Type your message:\n").lower()

while start is not False:
    caesar(text,shift,direction)
    programExe()
 
        