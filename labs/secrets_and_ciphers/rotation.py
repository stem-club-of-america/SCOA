#!/usr/bin/env python3
'''
Demonstrates the use of a rotation cipher to encrypt and decrypt
'''


def rot13(phrase):
    '''
    rot13(str) -> str

    This applies rot13 cipher to printable ASCII characters.
    '''
    output = []
    for c in phrase:
        num = ord(c)

        if num >= 65 and num <= 90:
            num -= 65
            num += 13
            num %= 26
            num += 65
            output.append(chr(num))
        elif num >= 97 and num <= 122:
            num -= 97
            num += 13
            num %= 26
            num += 97
            output.append(chr(num))
        else:
             output.append(c)

    return ''.join(output)

phrase = input("Enter something to rotate: ")

rot = rot13(phrase)
print("ENCRYPTED: {}".format(rot))

rot = rot13(rot)
print("DECRYPTED: {}".format(rot))
