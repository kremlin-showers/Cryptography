from chal1 import *
from chal2 import *
from chal3 import *



if __name__=='__main__':
    with open('4.txt', "r") as f:
        strings=f.readlines()
        decryptions=[]
        for currentstring in strings:
            currentstring=currentstring.strip()
            decryption=break_single_key(currentstring)
            decryptions.append(decryption)
    decryptions=sorted(decryptions, key=lambda x: x[0][0], reverse=True)
    for k in range(3):
        print(bytes.fromhex(decryptions[k][0][1]).decode('utf-8'))