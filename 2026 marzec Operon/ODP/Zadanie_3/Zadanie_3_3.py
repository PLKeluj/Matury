plik = open('pociagi.txt')
wagony = []

for i in plik:
    a, b = (i.strip()).split(' ')
    wagony.append([int(a), int(b)])

sklady_nos = {}

for i in wagony:
    wagon = i[0]
    nosnosc = i[1]

    if wagon not in sklady_nos:
        sklady_nos[wagon] = [nosnosc]
    else:
        sklady_nos[wagon].append(nosnosc)

wynik_nr = 0
wynik_nos = 0
wynik_wys = 0
for nr, nosnosci in sklady_nos.items():
    n = {}
    for i in nosnosci:
        if i not in n:
            n[i] = 1
        else:
            n[i] += 1
    w_nos = 0
    w_wys = 0
    for nos, wys in n.items():
        if wys > w_wys:
            w_nos = nos
            w_wys = wys

    if w_wys > wynik_wys:
        wynik_nr = nr
        wynik_nos = w_nos
        wynik_wys = w_wys

print(wynik_nr, wynik_nos, wynik_wys)