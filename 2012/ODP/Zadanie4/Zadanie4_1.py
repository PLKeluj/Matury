plikS = open("tj.txt", "r")
slowa = []
for linia in plikS:
    slowa.append(linia.strip())

plikK = open("klucze1.txt", "r")
klucze = []
for linia in plikK:
    klucze.append(linia.strip())

wynik = open('wynik4a.txt', 'w')

for i in range(len(slowa)):
    szyfrogram = ''
    slowo = slowa[i]
    klucz = klucze[i]
    for j in range(len(slowo)):
        nr = j % len(klucz)
        kod = ord(slowo[j]) + (ord(klucz[nr]) - 64)
        if kod > 90:
            kod -= 26
        szyfrogram += chr(kod)
    wynik.write(szyfrogram + "\n")
