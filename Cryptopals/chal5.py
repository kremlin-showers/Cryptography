from chal1 import *
from chal2 import *
from chal3 import *




def repeating_key_xor(hplain, hkey):
    while len(hkey) < len(hplain):
        hkey+=hkey
    hkey=hkey[:len(hplain)]
    return fixed_xor(hkey, hplain)



if __name__=='__main__':
    plain="It ain't hard to tell, I excel, then prevail The mic is contacted, I attract clientele"
    key="See you in Space"
    plainhex=plain.encode('utf-8').hex()
    hkey=key.encode('utf-8').hex()
    print(repeating_key_xor(plainhex, hkey))