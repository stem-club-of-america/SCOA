#!/usr/bin/env python3
'''
Encrypts and decrypts a phrase via substitution
'''

from string import printable
from random import shuffle

encrypt_sub = {}
decrypt_sub = {}

def generate_substitutions():
    '''
    generate_substitutions(NoneType) -> NoneType

    Generates a encryption and decryption dictionary
    '''
    global encrypt_sub
    global decrypt_sub

    characters = list(printable)
    shuffle(characters)

    encrypt_sub = {c:characters[i] for i,c in enumerate(printable)}
    decrypt_sub = {v:k for k,v in encrypt_sub.items()}

def encrypt(phrase):
    '''
    encrypt(str) -> str

    Encrypts a phrase
    '''
    enc = [encrypt_sub.get(c) for c in phrase]
    return ''.join(enc)

def decrypt(phrase):
    '''
    decrypt(str) -> str

    Decrypts a phrase
    '''
    dec = [decrypt_sub.get(c) for c in phrase]
    return ''.join(dec)

# generate the substitution dictionaries
generate_substitutions()

# get a phase to encrypt
phrase = input("Enter a phrase to encrypt and decrpyt: ")

# encrypt
enc = encrypt(phrase)
print("ENCRYPTED: {}".format(enc))

# decrypt
dec = decrypt(enc)
print("DECRYPTED: {}".format(dec))

