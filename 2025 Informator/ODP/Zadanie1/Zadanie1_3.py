plik = open('dane1_3.txt', 'r')
liczby = []

for i in plik:
    liczby.append(int(i.strip()))

print(liczby)