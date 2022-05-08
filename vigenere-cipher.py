# Vigenere Cipher is a block cipher where messages of blocks of length n,
# use keys of length n for encryption and decryption
import re
from transform import num_to_text, text_to_num, make_key


def encrypt(plaintext, secretkey):
    if len(plaintext) > len(secretkey):
        pt = text_to_num(plaintext)
        kw = make_key(plaintext, secretkey)
        encryption = [(pt[i] + kw[i]) % 26 for i in range(len(pt))]
        encryption = num_to_text(encryption)
        encryption = "".join(encryption)
        return ' '.join(re.findall('.{1,4}', encryption))
    else:
        print("Shorten keyword, try again.")


def decrypt(cyphertext, secretkey):
    ct = text_to_num(cyphertext)
    kw = make_key(cyphertext, secretkey)
    cypher_nums = [((ct[i] - kw[i]) % 26) for i in range(len(ct))]
    decryption = num_to_text(cypher_nums)
    return decryption


# Get message and key from user
ask = input("Encrypt(E) or Decrypt(D) a message?")
if ask.upper() == "E":
    plain_text = input('Enter the plaintext message to be encrypted: ').replace(" ", "")
    key_word = input("Enter the keyword for the message: ").replace(" ", "")
    print(encrypt(plain_text, key_word))
elif ask.upper() == "D":
    encrypted_text = input("Enter the encrypted message: ")
    key_word = input("Enter the keyword for the message: ")
    print(decrypt(encrypted_text, key_word))
else:
    print("Bad Input")
