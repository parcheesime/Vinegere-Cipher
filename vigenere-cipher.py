# Vigenere Cipher
import re

# Translate some text into ciphertext, each letter is represented by a numbered index
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# String of letters, transform to numbers
def text_to_num(text):
    nums = []
    text = text.lower()
    for p in text:
        for letter in alphabet:
            if p == letter:
                nums.append(alphabet.index(letter))
    return nums

# Numbers transform to letters
def num_to_text(nums):
    text = []
    for c in nums:
        for i in alphabet:
            if c == alphabet.index(i):
                text.append(i)
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
        encryption = [str((pt[i] + kw[i]) % 26) for i in range(len(pt))]
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
