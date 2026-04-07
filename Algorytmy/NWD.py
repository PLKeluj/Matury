a = 21
b = 7


def NWD(a, b):
    wynik = 1
    while a > b:
        a, b = b, a % b
        if b == 0:
            wynik = a
            return wynik
    return wynik

print(NWD(a, b))
