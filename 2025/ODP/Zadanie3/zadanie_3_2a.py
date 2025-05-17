plik = open('dron.txt', 'r')
ruchy = []

for i in plik:
    ruchy.append((i.strip()).split(' '))


odleglosc = 0
wysokosc = 0
wynik = 0
for ruch in ruchy:
    odleglosc += int(ruch[0])
    wysokosc += int(ruch[1])

    if (odleglosc > 0 and odleglosc < 5000) and (wysokosc > 0 and wysokosc < 5000):
        wynik += 1

print(wynik)
