from chal1 import *
from chal2 import *
import math

# https://en.wikipedia.org/wiki/Letter_frequency
english_letter_frequency = {
    'e': 12.70,
    't': 9.06,
    'a': 8.17,
    'o': 7.51,
    'i': 6.97,
    'n': 6.75,
    's': 6.33,
    'h': 6.09,
    'r': 5.99,
    'd': 4.25,
    'l': 4.03,
    'c': 2.78,
    'u': 2.76,
    'm': 2.41,
    'w': 2.36,
    'f': 2.23,
    'g': 2.02,
    'y': 1.97,
    'p': 1.93,
    'b': 1.29,
    'v': 0.98,
    'k': 0.77,
    'j': 0.15,
    'x': 0.15,
    'q': 0.10,
    'z': 0.07
    }

# Here we score hex strings directly
def score_hex_string(hstr):
    # We consider each charecter that is a letter.
    alphabet="abcdefghijklmnopqrstuvwxyz"
    hstr_letter_frequency={}
    for char in alphabet:
        hstr_letter_frequency[char]=0
    total_charecters=0
    try:
        charstring=bytes.fromhex(hstr).decode('utf-8')
        for char in charstring:
            if char.isprintable()==False and char != "\n":
                return 0
            if char.isalpha():
                hstr_letter_frequency[char.lower()]+=1

        for i in hstr_letter_frequency:
            hstr_letter_frequency[i]/=len(charstring)
        score=0
        for i in hstr_letter_frequency:
            score+=math.sqrt(hstr_letter_frequency[i] * english_letter_frequency[i] / 100)
        return score

    except:
        return 0


def break_single_key(hcipher, candidates=1):
    keys=[]
    decryptions=[]
    for i in range(32,126,1):
        current_key=hex(i)[2:]
        current_key=current_key * (len(hcipher) // 2)
        keys.append(current_key)
    for key in keys:
        current_decryption=fixed_xor(hcipher, key)
        decryptions.append((score_hex_string(current_decryption), current_decryption, key))
    decryptions=sorted(decryptions, key=lambda x: x[0], reverse=True)
    return decryptions[:candidates]




if __name__=='__main__':
    # hstring="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    # decryptions=break_single_key(hstring)
    # print(decryptions)
    # print(decryptions[0][1])
    # print(bytes.fromhex(decryptions[0][1]).decode('utf-8'))

    print(bytes.fromhex('426e67652020756974756b6e6e620a67637a776e2061617961776d65747561766f206576757474206c777274206c736b6765206c6e736c').decode('utf-8'))
    print(score_hex_string('426e67652020756974756b6e6e620a67637a776e2061617961776d65747561766f206576757474206c777274206c736b6765206c6e736c'))