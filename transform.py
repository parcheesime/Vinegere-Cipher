import string

# Each letter represented by index in alphabet list
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
