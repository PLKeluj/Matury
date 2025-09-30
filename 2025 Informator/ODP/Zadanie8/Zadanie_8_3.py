plik = open('dane8.txt', 'r')

liczby = []
for i in plik:
    liczby.append(int(i.strip()))

wynik = 0
t = 1

for i in range(len(liczby) - 1):
    if liczby[i] < liczby[i + 1]:
        t += 1
    else:
        if t > wynik:
            wynik = t
        t = 1

print(wynik)
