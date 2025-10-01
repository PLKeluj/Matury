plik = open('dane1_3.txt', 'r')
liczby = []

for i in plik:
    liczby.append(int(i.strip()))

max = 0

for i in range(len(liczby)):
    for j in range(i + 1, len(liczby)):
        x = i
        suma = 0
        while x <= j:
            suma += liczby[x]
            x += 1
        if suma > max:
            max = suma

print(max)
