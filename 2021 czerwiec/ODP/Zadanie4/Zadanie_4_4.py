plik = open('napisy.txt')
liczby = []
for linia in plik:
    linia = linia.strip()
    liczba = ''
    for cyfra in linia:
        if cyfra.isdigit():
            liczba += cyfra
        if len(liczba) == 2:
            liczby.append(liczba)
            liczba = ''

haslo = ''
licznik = 0
for liczba in liczby:
    liczba = int(liczba)
    if 65 <= liczba <= 90:
        litera = chr(liczba)
        if licznik == 3:
            break
        if litera == 'X':
            licznik += 1
        haslo += litera

print(haslo)
