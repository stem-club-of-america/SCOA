![SCOA](https://github.com/stem-club-of-america/SCOA/blob/main/images/SCOA_Logo_Small.png)

# Secrets and Ciphers
In this lab we'll work with text rotations and substitutions.  We'll discover ASCII and some basic ways in which we can implement simple ciphers to hide our messages.

## Difficulty
2 / 5

## ASCII
ASCII, abbreviated from American Standard Code for Information Interchange, is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices. Most modern character-encoding schemes are based on ASCII, although they support many additional characters.

```text
Dec Hex    Dec Hex    Dec Hex  Dec Hex  Dec Hex  Dec Hex   Dec Hex   Dec Hex
  0 00 NUL  16 10 DLE  32 20    48 30 0  64 40 @  80 50 P   96 60 `  112 70 p
  1 01 SOH  17 11 DC1  33 21 !  49 31 1  65 41 A  81 51 Q   97 61 a  113 71 q
  2 02 STX  18 12 DC2  34 22 "  50 32 2  66 42 B  82 52 R   98 62 b  114 72 r
  3 03 ETX  19 13 DC3  35 23 #  51 33 3  67 43 C  83 53 S   99 63 c  115 73 s
  4 04 EOT  20 14 DC4  36 24 $  52 34 4  68 44 D  84 54 T  100 64 d  116 74 t
  5 05 ENQ  21 15 NAK  37 25 %  53 35 5  69 45 E  85 55 U  101 65 e  117 75 u
  6 06 ACK  22 16 SYN  38 26 &  54 36 6  70 46 F  86 56 V  102 66 f  118 76 v
  7 07 BEL  23 17 ETB  39 27 '  55 37 7  71 47 G  87 57 W  103 67 g  119 77 w
  8 08 BS   24 18 CAN  40 28 (  56 38 8  72 48 H  88 58 X  104 68 h  120 78 x
  9 09 HT   25 19 EM   41 29 )  57 39 9  73 49 I  89 59 Y  105 69 i  121 79 y
 10 0A LF   26 1A SUB  42 2A *  58 3A :  74 4A J  90 5A Z  106 6A j  122 7A z
 11 0B VT   27 1B ESC  43 2B +  59 3B ;  75 4B K  91 5B [  107 6B k  123 7B {
 12 0C FF   28 1C FS   44 2C ,  60 3C <  76 4C L  92 5C \  108 6C l  124 7C |
 13 0D CR   29 1D GS   45 2D -  61 3D =  77 4D M  93 5D ]  109 6D m  125 7D }
 14 0E SO   30 1E RS   46 2E .  62 3E >  78 4E N  94 5E ^  110 6E n  126 7E ~
 15 0F SI   31 1F US   47 2F /  63 3F ?  79 4F O  95 5F _  111 6F o  127 7F DEL
```

## Rotation Cipher
We'll use a rot13 (rotate 13) cipher.  This is an easy cipher because the alphabet has 26 characters.  If we rotate 13 characters to the right, you have your cipher character and rotate 13 again and you have your original character.  We'll apply this logic using the ASCII decimal values above.

```python3
def rot13(phrase):
    '''
    rot13(str) -> str

    This applies rot13 cipher to printable ascii characters.
    '''
    output = []
    for c in phrase:
        num = ord(c)

        # Uppercase characters
        if num >= 65 and num <= 90:
            num -= 65
            num += 13
            num %= 26
            num += 65
            output.append(chr(num))
        # Lowercase characters
        elif num >= 97 and num <= 122:
            num -= 97
            num += 13
            num %= 26
            num += 97
            output.append(chr(num))
        # Everything else
        else:
             output.append(c)

    return ''.join(output)
```

## Substitution Cipher
Substitution ciphers are about replacing each group of plain-text letters with another predefined group. For decrypting, one should use a reverse substitution.

```python 3
from string import printable
from random import shuffle

def generate_substitutions():
    '''
    generate_substitutions(NoneType) -> NoneType

    Generates a encryption and decryption dictionary
    '''
    global encrypt_sub
    global decrypt_sub

    characters = list(printable)
    shuffle(characters)

    # Generator comprehensions look odd but are fast and efficient
    encrypt_sub = {c:characters[i] for i,c in enumerate(printable)}
    decrypt_sub = {v:k for k,v in encrypt_sub.items()}
```

## XOR
XOR or Exclusive OR is a bitwise (works on the individual bits of number) operation. See the truth table below for *AND*, *OR*, and *XOR*:

### AND
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

### OR
0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
1 | 1 = 1

### XOR
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

When the bits are different, *XOR* returns a 1. When the bits are the same, it returns a 0.  Because of this phenomenon, we can *XOR* with a key to encrypt, and *XOR* with the same key a second time to decrypt.

```python3
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
```
