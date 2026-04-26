plik = open('pociagi.txt')
wagony = []

for i in plik:
    a, b = (i.strip()).split(' ')
    wagony.append([int(a), int(b)])

sklady_dl = {}
sklady_nos = {}

for i in wagony:
    wagon = i[0]
    nosnosc = i[1]

    if wagon not in sklady_dl:
        sklady_dl[wagon] =1
    else:
        sklady_dl[wagon] +=1

    if wagon not in sklady_nos:
        sklady_nos[wagon] = nosnosc
    else:
        sklady_nos[wagon] += nosnosc

wynik_wagon = 0
wynik_dlugosc = 0
wynik_nosnosc = 0
for wagon, dlugosc in sklady_dl.items():
    if dlugosc> wynik_dlugosc:
        wynik_wagon = wagon
        wynik_dlugosc = dlugosc
        wynik_nosnosc = sklady_nos[wagon]

print(wynik_wagon, wynik_dlugosc, wynik_nosnosc)