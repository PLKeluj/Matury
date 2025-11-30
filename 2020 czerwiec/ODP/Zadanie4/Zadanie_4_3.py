plik = open('pary.txt')
wynik = open('odp_4_3.txt', 'w')
liczby = []
slowa = []

for i in plik:
    liczba, slowo = i.split(' ')
    liczby.append(int(liczba.strip()))
    slowa.append(slowo.strip())

para = [100, 0]
for i in range(len(slowa)):
    if liczby[i] == len(slowa[i]):
        if liczby[i] < para[0]:
            para = [liczby[i], slowa[i]]
        elif liczby[i] == para[0]:
            dl1 = len(slowa[i])
            dl2 = len(para[1])
            dl = dl2
            if dl1 < dl2:
                dl = dl1
            for x in range(dl):
                if ord(slowa[i][x]) > ord(para[1][x]):
                    break
                elif ord(slowa[i][x]) < ord(para[1][x]):
                    para = [liczby[i], slowa[i]]
                    break

                if x == dl-1:
                    if dl1 < dl2:
                        para = [liczby[i], slowa[i]]

wynik.write(f'{para[0]} {para[1]}')
