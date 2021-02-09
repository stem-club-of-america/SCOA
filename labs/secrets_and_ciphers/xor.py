#!/usr/bin/env python3
'''
demonstrates the use of xor for encryption and decryption
'''

def xor(phrase, key):
    '''
    xor(str, str) -> str

    Applies xor to a phrase using a key
    '''
    # there should be at least one character
    length = len(key)
    if length == 0:
        return None

    output = []
    for i,c in enumerate(phrase):
        # in case the key is smaller than the phrase, we'll keep looping
        # the key using the modulus operator
        num = ord(c) ^ ord(key[i % length])
        output.append(chr(num))

    return ''.join(output)


phrase = input("Enter something to encrypt: ")
key = input("Enter a key: ")

enc = xor(phrase, key)
print("ENCRYPTED: {}".format(enc))

if enc is not None:
    dec = xor(enc, key)
    print("DECRYPTED: {}".format(dec))
