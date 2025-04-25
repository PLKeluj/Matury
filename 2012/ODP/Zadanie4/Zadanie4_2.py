plikS = open("sz.txt", "r")
slowa = []
for linia in plikS:
    slowa.append(linia.strip())

plikK = open("klucze2.txt", "r")
klucze = []
for linia in plikK:
    klucze.append(linia.strip())

wynik = open('wynik4b.txt', 'w')

for i in range(len(slowa)):
    deszyfr = ''
    slowo = slowa[i]
    klucz = klucze[i]
    for j in range(len(slowo)):
        nr = j % len(klucz)
        kod = ord(slowo[j]) - ord(klucz[nr]) + 64
        if kod < 64:
            kod += 26
        deszyfr += chr(kod)
    wynik.write(deszyfr + "\n")
