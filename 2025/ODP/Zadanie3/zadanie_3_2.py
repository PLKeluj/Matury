plik = open('dron.txt')

ruchy = []
for i in plik:
    i = i.strip()
    ruchy.append(i.split(' '))

# PODPUNKT A
aktualna_pozycja = [0, 0]
pozycje = []
wynik_a = 0
for i in ruchy:
    aktualna_pozycja[0] += int(i[0])
    aktualna_pozycja[1] += int(i[1])
    pozycje.append([int(str(aktualna_pozycja[0])), int(str(aktualna_pozycja[1]))])

    if 0 < aktualna_pozycja[0] < 5000 and 0 < aktualna_pozycja[1] < 5000:
        wynik_a += 1

print(wynik_a)

# PODPUNKT B
for i in range(0, len(pozycje) - 2):
    for j in range(i + 2, len(pozycje)):
        srodek = [(pozycje[i][0] + pozycje[j][0]) / 2, (pozycje[i][1] + pozycje[j][1]) / 2]
        if srodek in pozycje:
            print(pozycje[i], srodek, pozycje[j])
