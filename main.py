# Vigenere Cipher

# Translate some text into ciphertext, each letter is represented by a numbered index
def text_to_num(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    cipher = []
    for p in text:
        for l in alphabet:
            if p == l:
                cipher.append(alphabet.index(l))
    return cipher


def encrypt(plaintext, keyword):
    pt = text_to_num(plaintext)
    kw = text_to_num(keyword)


def decrypt(cyphertext, keyword):
    pass


ask = input("Encrypt(E) or Decrypt(D) a message?")
if ask.upper() == "E":
    plaintext = input('Enter the plaintext message to be encrypted: ')
    keyword = input("Enter the keyword for the message: ")
    print(text_to_num(plaintext))
    print(text_to_num(keyword))
elif ask.upper() == "D":
    cyphertext = input("Enter the encrypted message: ")
    keyword = input("Enter the keyword for the message: ")

else:
    print("Bad Input")


