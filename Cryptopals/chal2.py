from chal1 import *



# Takes the fixed xor of two hex strings.
def fixed_xor(ha, hb):
    assert len(ha)==len(hb)
    output=[]
    for i in range(len(ha)):
        output.append(hex(int(ha[i], 16) ^ int(hb[i], 16))[2:])
    return ''.join(i for i in output)



if __name__=='__main__':
    string1='1c0111001f010100061a024b53535009181c'
    strnig2='686974207468652062756c6c277320657965'
    print(fixed_xor(string1, strnig2))