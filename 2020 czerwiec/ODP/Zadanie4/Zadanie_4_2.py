plik = open('pary.txt')
wynik = open('odp_4_2.txt', 'w')
liczby = []
slowa = []

for i in plik:
    liczba, slowo = i.split(' ')
    liczby.append(int(liczba.strip()))
    slowa.append(slowo.strip())

for slowo in slowa:
    max_dl = 0
    dl = 1
    ciag = ''
    for i in range(len(slowo) - 1):
        if slowo[i] == slowo[i + 1]:
            dl += 1
        else:
            if dl > max_dl:
                max_dl = dl
                ciag = dl * f'{slowo[i]}'
                dl = 1
        if i == len(slowo) - 2:
            if dl > max_dl:
                max_dl = dl
                ciag = dl * f'{slowo[i]}'
                dl = 1

    wynik.write(f'{ciag} {max_dl} \n')
