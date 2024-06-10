from chal1 import *
from chal2 import *
from chal3 import *
from chal4 import *
from chal5 import *


# The input to these strings must be in hex
def h_distance(str1, str2):
    assert len(str1) == len(str2)
    distance = 0
    for i in range(len(str1)):
        x = int(str1[i], 16)
        y = int(str2[i], 16)
        distance += bin(x ^ y).count("1")
    return distance


# This function gives a 'score' for each keysize guess


def sizescore(hcipher, keysize):
    blocks = []
    # breaks the hcipher into blocks of keysize bytes
    for i in range(0, len(hcipher) // (2 * keysize)):
        blocks.append(hcipher[i * 2 * keysize : (i + 1) * 2 * keysize])
    distances = 0
    n = 0
    for i in range(0, len(blocks)):
        for j in range(i + 1, len(blocks)):
            distances += h_distance(blocks[i], blocks[j])
            n += 1
    normalised_distance = distances / (n * keysize)
    return normalised_distance


def findsize(hcipher, ncandidates=1):
    scores = []
    for i in range(2, 40):
        scores.append((sizescore(hcipher, i), i))
    scores = sorted(scores, key=lambda x: x[0])
    return scores[:ncandidates]


# Solves repeating key xor given the keylength
def solvexor(hcipher, keylen):
    strings = []
    keys = []
    decrypted_blocks = []
    for i in range(keylen):
        j = 2 * i
        current_output = ""
        while j < len(hcipher):
            current_output += hcipher[j : j + 2]
            j += 2 * keylen
        strings.append(current_output)
    for i in strings:
        current_sol = break_single_key(i)
        decrypted_blocks.append(current_sol[0][1])
        keys.append(current_sol[0][2])
    fin_key = ""
    for j in range(len(keys)):
        fin_key += keys[j][:2]
    # print(bytes.fromhex(fin_key).decode('utf-8'))
    # print(bytes.fromhex(repeating_key_xor(hcipher, fin_key)).decode('utf-8'))
    return (fin_key, repeating_key_xor(hcipher, fin_key))


def generalsolvexor(hcipher, ncandidates=5):
    keysizes = findsize(hcipher, ncandidates)
    solutions = []
    for x in keysizes:
        solutions.append(solvexor(hcipher, x[1]))
    solutions = sorted(solutions, key=lambda x: score_hex_string(x[1]), reverse=True)
    return solutions


if __name__ == "__main__":
    s1 = "this is a test"
    s2 = "wokka wokka!!!"
    h1 = s1.encode("utf-8").hex()
    h2 = s2.encode("utf-8").hex()
    x = h_distance(h1, h2)
    assert x == 37
    with open("6.txt", "r") as f:
        string = f.read()
        string = string.replace("\n", "")
        string = string.strip()
        string = b642hex(string)
        solutions = generalsolvexor(string)
        print(
            f"Key:{bytes.fromhex(solutions[0][0]).decode('utf-8')}\n Text:\n{bytes.fromhex(solutions[0][1]).decode('utf-8')}"
        )
