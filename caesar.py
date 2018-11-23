code = "PDA MQEYG XNKSJ BKT FQILO KRAN PDA HWVU ZKC KB YWAOWN WJZ UKQN QJEMQA OKHQPEKJ EO AZNIKDKAHALL"
range_val = 26


def decrypt(str_val, n_val):
    decrypted = ""
    for ch in str_val:
        if ch.isspace():
            decrypted += " "
        else:
            ascii_val = ord(ch) + n_val
            if ascii_val > 90:
                ascii_val -= range_val
            decrypted += chr(ascii_val)
    return decrypted


def search_move(str_val, begin, end):
    for i in range(begin, end):
        print("Move value is %s" % i)
        print decrypt(str_val, i) + "\n"


if __name__ == '__main__':
    print search_move(code, -3, 6)