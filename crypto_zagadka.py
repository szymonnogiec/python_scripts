import string
import base64
import httplib

input = """tO JESt NASza PiERWszA crYpTo zagwozdka ZgAdnij uKrytY PRZeKAZ uzytY AlFaBEt tO litery az OrAZ znaki"""

range_val = 26

alpha = string.ascii_lowercase + '!,./;?'

line_1 = 'tO JESt NASza PiERWszA crYpTo zagwozdka'
line_2 = 'ZgAdnij uKrytY PRZeKAZ'
line_3 = 'uzytY AlFaBEt tO litery az OrAZ znaki ! ? . , ; /'

def make_rot_n(n):
 lc = string.ascii_lowercase
 uc = string.ascii_uppercase
 trans = string.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
 return lambda s: string.translate(s, trans)



###  a-z: 97-122, 33, 44, 46, 47. 59, 63
def decrypt(str_val, n_val):
    rot = make_rot_n(n_val)
    decrypted = ""
    for ch in str_val:

        ascii_val = ord(ch) + n_val
        if ascii_val > 127:
            ascii_val = ascii_val - 127

        if ascii_val < 0:
            ascii_val = ascii_val + 127

        shifted_char = chr(ascii_val)
        if shifted_char in alpha:
            decrypted += chr(ascii_val)

    return decrypted

def decrypt_2(str_val, n_val):
    size = len(alpha)
    result = ''
    for ch in str_val:
        index = alpha.find(ch)
        if index is not -1:
            new_index = index + n_val
            result += alpha[new_index % size]

    return result

def decrypt_3(str_val, n_val):


def search_move(str_val, begin, end):
    for i in range(begin, end):
        # print("Move value is %s" % i)
        print i
        print decrypt_2(str_val, i)


def main():
    l1u = line_1.translate(None, string.ascii_lowercase)
    l1l = line_1.translate(None, string.ascii_uppercase)
    l1 = l1u + l1l
    l2u = line_2.translate(None, string.ascii_lowercase)
    l2l = line_2.translate(None, string.ascii_uppercase)
    l2 = l2u + l2l
    l3u = line_3.translate(None, string.ascii_lowercase)
    l3l = line_3.translate(None, string.ascii_uppercase)
    l3 = l3u + l3l

    l = l1 + l2 + l3
    search_move(l.lower(), -1, 31)

if __name__ == '__main__':
    main()
