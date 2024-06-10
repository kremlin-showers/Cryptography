# The Problem

We are given a few ciphertexts all of which have been encrypted using the following code

```python
import sys

MSGS = ( ---  11 secret messages  --- )

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]
```


# Solution
We notice that xoring two ciphertexts will be the same as the xor of their messages

$$c_1 \oplus c_2 = (m_1 \oplus k) \oplus (m_2 \oplus k) = m_1 \oplus m_2$$
Also another interesting observation (given by the question setters) is that xoring any alphabetical charecter with space leads to another alphabetical charecter (small becomes capital). This means that for any of the ciphertexts if the a location , when xored with all other ciphertexts leads to zero or alphabetical charecters then that location in that specific ciphertext's plaintext must be a space (or is quite likely to be). This means that we can get the corresponding location's key value and hence decipher that index in all ciphertexts.
Just doing this leads to the following decryption ~ is a placeholder
```
We~can aac~or ~he num~er ~~ wi~~~~~~~tu~~~~mputer~~ We~can also factor the number~~
Eu~er whul~ pr~bably ~njo~~tha~~~~~~~is~~~~orem b~~ome~ a corner stone of crypto ~~
Th~ nicb t~ing~about ~eey~~q i~~~~~~~e ~~~~tograp~~rs ~an drive a lot of fancy ca~~
Th~ cipoer~ext~produc~d b~~a w~~~~~~~ry~~~~n algo~~thm~looks as good as ciphertex~~
Yo~ don t ~ant~to buy~a s~~ of~~~~~~~ys~~~~m a gu~~who~specializes in stealing ca~~
Th~re aue ~wo ~ypes o~ cr~~tog~~~~~~~ t~~~~which ~~ll ~eep secrets safe from your~~
Th~re aue ~wo ~ypes o~ cy~~ogr~~~~~~~ne~~~~t allo~~ th~ Government to use brute f~~
We~can tee~the~point ~her~~the~~~~~~~s ~~~~ppy if~~ wr~ng bit is sent and consume~~
A ~privfte~key~  encr~pti~~ sc~~~~~~~at~~~~ algor~~hms~ namely a procedure for ge~~
 T~e Coici~e O~fordDi~tio~~ry ~~~~~~~de~~~~es cry~~o a~ the art of  writing o r s~~
Th~ secuet~mes~age is~ Wh~~ us~~~~~~~tr~~~~cipher~~nev~r use the key more than on~~
```
Now we can guess the remaining spots manually. For example the third index in the first plaintext is definitely a space etc.
to get the final plaintexts as follows


We can factor the number 15 with quantum computers. We can also factor the number 1
Euler would probably enjoy that now his theorem becomes a corner stone of crypto - 
The nice thing about Keeyloq is now we cryptographers can drive a lot of fancy cars
The ciphertext produced by a weak encryption algorithm looks as good as ciphertext 
You don't want to buy a set of car keys from a guy who specializes in stealing cars
There are two types of cryptography - that which will keep secrets safe from your l
There are two types of cyptography: one that allows the Government to use brute for
We can see the point where the chip is unhappy if a wrong bit is sent and consumes 
A (private-key)  encryption scheme states 3 algorithms, namely a procedure for gene
 The Concise OxfordDictionary (2006) deï¬nes crypto as the art of  writing o r sol
The secret message is: When using a stream cipher, never use the key more than once