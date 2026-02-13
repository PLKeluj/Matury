plik = open('odbiorcy.txt')
plikw = open('wynik_4_2.txt', 'w')
odbiorcy = []
nr_komputerow = []
licznik = 0
for i in plik:
    odbiorcy.append(int(i.strip()))
    licznik += 1
    nr_komputerow.append(licznik)

wynik = 0
for i in nr_komputerow:
    if i not in odbiorcy:
        wynik += 1

plikw.write(str(wynik))