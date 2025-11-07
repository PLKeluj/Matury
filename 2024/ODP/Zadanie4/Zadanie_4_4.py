plik = open('liczby.txt', 'r')
liczby = []

for wiersz in plik:
    l = []
    wiersz = wiersz.split(' ')
    for i in wiersz:
        l.append(int(i.strip()))
    liczby.append(l)

liczby_p = liczby[0]
liczby_c = liczby[1]

srednie = [0] * (len(liczby_p) - 49)
for i in range(len(liczby_p) - 49):
    srednie[i] = ([0] * (len(liczby_p) - i - 49))


def suma(liczby):
    suma = 0
    for i in liczby:
        suma += i
    return suma


for i in range(len(liczby_p) - 49):
    x = 0
    for j in range(i + 49, len(liczby_p)):
        d = j - i + 1
        if d == 50:
            srednie[i][x] = suma(liczby_p[i:(j + 1)]) / d
            d_p = d
            x += 1
        else:
            srednie[i][x] = round(((((srednie[i][x - 1]) * d_p) + liczby_p[j]) / d), 100)
            d_p = d
            x += 1

max = 0
a = 0
b = 0
for i in range(len(srednie)):
    for j in range(len(srednie) - i):
        if srednie[i][j] > max:
            max = srednie[i][j]
            a = i
            b = j

print(max, b + 50, liczby_p[a])
