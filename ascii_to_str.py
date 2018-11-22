codes = "84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 102, 103, 100, 110, 108, 100, 98, 114, 109, 109, 110, 97"
separator = ','


def decode_numbers(str):
    list = str.split(separator)
    result = ""
    for i in list:
        result += chr(int(i))
    print result


if __name__ == '__main__':
    decode_numbers(codes)