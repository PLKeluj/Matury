w = 1
k = 3
n = 19


def dziesietna_do_binarnej(n):
    wynik = 0
    potega = 2
    while potega < n:
        potega *= 2
    potega = potega // 2

    while n > 0:
        if n - potega >= 0:
            wynik = wynik * 10 + 1
            n = n - potega
        else:
            wynik = wynik * 10
        potega = potega // 2

    return wynik


bin = dziesietna_do_binarnej(n)
dl = 0
while bin > 0:
    bin = bin // 10
    dl += 1

wielkosc = w * k
nr_wyrazu = wielkosc % dl
bin = dziesietna_do_binarnej(n)

if nr_wyrazu == 0:
    x = bin % 10
else:
    licznik = 1
    while (dl - nr_wyrazu + 1) != licznik:
        licznik += 1
        bin = bin // 10
    x = bin % 10

print(x)
