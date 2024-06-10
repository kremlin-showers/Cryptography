from base64 import b64decode, b64encode


def hex2b64(hex_string):
    return b64encode(bytes.fromhex(hex_string)).decode()


def b642hex(base_64_string):
    return b64decode(base_64_string).hex()


if __name__ == "__main__":
    test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex2b64(test))
    print(b642hex(hex2b64(test)))

