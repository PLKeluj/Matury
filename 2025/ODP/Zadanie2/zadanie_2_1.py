symbole = []
plik = open('symbole.txt', 'r')

for i in plik:
    symbole.append(i.strip())

wynik = []
for wiersz in symbole:
    zgodnosc = 0
    x = 0
    while wiersz[x] == wiersz[11-x] and x <=5:
        zgodnosc += 1
        x += 1

    if zgodnosc == 6:
        wynik.append(wiersz)

print(wynik)
