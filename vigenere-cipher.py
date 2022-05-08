# Vigenere Cipher
import re
import string

# Translate some text into ciphertext, each letter is represented by a numbered index
alphabet = list(string.ascii_lowercase)

# String of letters, transform to numbers
def text_to_num(text):
    text = text.lower()
    nums = [alphabet.index(letter) for p in text for letter in alphabet if p == letter]
    return nums

# Numbers transform to letters
def num_to_text(nums):
    text = [i for c in nums for i in alphabet if c == alphabet.index(i)]
    return "".join(text)


# Generate the keyword
# Take the secret key and extend it to the length of the message
def make_key(plaintext, secretkey):
    add_on = len(plaintext) - len(secretkey)
    key_list = text_to_num(secretkey)
    for k in range(add_on):
        key_list.append(key_list[k])
    return key_list


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
