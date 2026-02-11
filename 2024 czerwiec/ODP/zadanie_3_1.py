plik = open('slowa.txt')
plikw = open('wynik_3_1.txt', 'w')
slowa = []
for i in plik:
    slowa.append(i.strip())

wynik = 0
for i in slowa:
    flaga = 1
    for x in range(len(i)-2):
        if flaga == 1 and i[x] == 'k' and i[x+2] == 't':
            wynik += 1
            flaga = 0

plikw.write(str(wynik))