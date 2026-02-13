plik = open('slowa.txt')
plikw = open('wynik_3_2.txt', 'w')
slowa = []
for i in plik:
    slowa.append(i.strip())


def rot(slowo):
    wynik = ''
    for litera in slowo:
        nr = ord(litera)
        if nr + 13 > 122:
            nr = 96 - (122 - (nr + 13))
        else:
            nr = nr + 13

        wynik += chr(nr)
    return wynik

wynik = 0
max = 0
sl = ''
for i in slowa:
    if rot(i) == i[::-1]:
        wynik += 1
        if len(i) > max:
            max = len(i)
            sl = i

print(wynik)
print(sl)

plikw.write(f'{str(wynik)}\n')
plikw.write(str(sl))