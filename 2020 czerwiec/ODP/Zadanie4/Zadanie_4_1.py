plik = open('pary.txt')
wynik = open('odp_4_1.txt', 'w')
liczby = []
slowa = []

for i in plik:
    liczba, slowo = i.split(' ')
    liczby.append(int(liczba.strip()))
    slowa.append(slowo.strip())

pierwsze = [1] * 101
pierwsze[0] = 0
pierwsze[1] = 0
for i in range(2, 10):
    j = i
    if pierwsze[i] == 1:
        i = i * i
        pierwsze[i] = 0
        while i < 100 - j + 1:
            i = i + j
            pierwsze[i] = 0

p = []
for i in range(len(pierwsze)):
    if pierwsze[i] == 1:
        p.append(i)

pierwsze = p


def suma_pierwszych(liczba):
    w = [0, 0]
    i = 0
    while pierwsze[i] < liczba and liczba - pierwsze[i] != 1:
        i += 1

    i -= 1
    reszta = liczba - pierwsze[i]

    if reszta in pierwsze:
        w[0], w[1] = reszta, pierwsze[i]

        return f'{w[0]} {w[1]} '


for i in liczby:
    if i % 2 == 0 and i > 4:
        w = suma_pierwszych(i)
        if w != None:
            wynik.write(f'{i} {w} \n')
