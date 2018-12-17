
#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
#Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

import logging
import re

# global variables
the = re.compile(r"the", re.IGNORECASE)
letters = [ord(x) for x in "abcdefghijklmnopqrstuvwxyz"]
english = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[]\\,./`~!@#$%^&*()_+{}|:"<>? \n\t';'''
eng_set = set([ord(x) for x in english])

def Decode(k, enc):
    key = k*402
    for i in range(len(enc)):
        key[i] = key[i] ^ enc[i]
    nw = 0
    for d in key:
        if (not d in eng_set):
            return 0
    dec =[chr(x) for x in key]
    s = ''.join(dec)
#    return s
    if (the.search(s)):
        return s
    return 0

def main(args):
    txt = open('data/p059_cipher.txt').read()
    enc = [int(x) for x in txt.split(',')]

    s = []
    letters = [ord(x) for x in '''abcdefghijklmnopqrstuvwxyz''']
    for a in letters:
        for b in letters:
            for c in letters:
                dec = Decode([a,b,c], enc)
                if (dec):
                    print(dec)
                    s.append(sum([ord(x) for x in dec]))

    logging.debug(s)

    dec = Decode([ord(x) for x in 'god'], enc)
    logging.debug(dec[:-5])
    logging.info(sum([ord(x) for x in dec[:-5]]))
    for c in dec:
        if (not ord(c) in eng_set):
            logging.info(c, ord(c))
            