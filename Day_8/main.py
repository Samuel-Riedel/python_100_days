alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encoded_word = []


def encrypt(text,shift):
    for i in text:
        index_text = alphabet.index(i)
        index_text += shift 
        encoded_word.append(alphabet[index_text])
        #print(f"The encoded message is: {alphabet[index_text]}")
    print("".join(encoded_word))



def decrypt(text,shift):
    for i in text:
        index_text = alphabet.index(i)
        index_text -= shift 
        encoded_word.append(alphabet[index_text])
        #print(f"The encoded message is: {alphabet[index_text]}")
    print("".join(encoded_word))

decrypt(text,shift)
