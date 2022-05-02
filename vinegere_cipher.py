# Vigenere Cipher
import re
# Translate some text into ciphertext, each letter is represented by a numbered index
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def text_to_num(text):
    cipher = []
    text = text.lower()
    for p in text:
        for l in alphabet:
            if p == l:
                cipher.append(alphabet.index(l))
    return cipher


def num_to_text(nums):
    for c in nums:
       plain = [i for i in alphabet if c == alphabet.index(i)]
    return plain


def make_key(plaintext, keyword):
    add_on = len(plaintext) - len(keyword)
    key_list = text_to_num(keyword)
    for k in range(add_on):
        key_list.append(key_list[k])
    return key_list


def encrypt(plaintext, keyword):
    pt = text_to_num(plaintext)
    kw = make_key(plaintext, keyword)
    encryption = [str((pt[i] + kw[i]) % 26) for i in range(len(pt))]
    encryption = "".join(encryption)
    return ' '.join(re.findall('.{1,4}', encryption))


def decrypt(cyphertext, keyword):
    pass


ask = input("Encrypt(E) or Decrypt(D) a message?")
if ask.upper() == "E":
    plain_text = input('Enter the plaintext message to be encrypted: ').replace(" ", "")
    key_word = input("Enter the keyword for the message: ").replace(" ", "")
    print("Length of message: {}".format(len(text_to_num(plain_text))))
    print("Length of key: {}".format(len(make_key(plain_text, key_word))))
    print(encrypt(plain_text, key_word))
elif ask.upper() == "D":
    cyphertext = input("Enter the encrypted message: ")
    keyword = input("Enter the keyword for the message: ")

else:
    print("Bad Input")
