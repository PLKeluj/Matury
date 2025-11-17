liczba_d = 123
liczba_h = '7B'
d_hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def dec_to_hex(liczba):
    wynik = ''
    i = 0
    while liczba > 0:
        cyfra = (liczba % 16)
        if cyfra < 10:
            wynik = str(cyfra) + wynik
        else:
            wynik = d_hex[cyfra] + wynik

        i += 1
        liczba //= 16

    return wynik


print(dec_to_hex(liczba_d))


def hex_to_dec(liczba):
    wynik = 0
    i = 0
    for z in range(len(liczba)):
        if liczba[-+1] not in hex_d:
            x = int(liczba[-1])
        else:
            x = int(hex_d[liczba[-1]])

        cyfra = x * (16 ** i)
        wynik += cyfra

        i += 1
        liczba = liczba[:-1]

    return wynik


print(hex_to_dec(liczba_h))
