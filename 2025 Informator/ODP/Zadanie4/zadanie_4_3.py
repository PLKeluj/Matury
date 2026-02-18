plik = open('dane4.txt')
liczby = []
for i in plik:
    liczby.append(int(i.strip()))

max = 0
wynik = 0

for i in range(1, len(liczby)):
    temp = 0
    for j in range(i):
        if i > j and liczby[i] > liczby[j]:
            temp += 1

    if temp > max:
        max = temp
        wynik = i + 1

print(wynik)
