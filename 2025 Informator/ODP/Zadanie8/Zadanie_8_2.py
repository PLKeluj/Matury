plik = open('dane8.txt', 'r')

liczby = []
for i in plik:
    liczby.append(int(i.strip()))

wynik = 0

for i in range(len(liczby)):
    for j in range(i + 1, len(liczby)):
        if liczby[i] > liczby[j]:
            wynik += 1

print(wynik)
