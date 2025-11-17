t = 'cbbd'


def czyPalindrom(tekst):
    dlugosc = len(tekst)
    pol = int(dlugosc // 2)

    for i in range(pol):
        if tekst[i] != tekst[dlugosc - (i+1)]:
            return False
    return True


def najdluzszyPalindrom(ciag):
    wynik_max = 0
    tekst_max = ''

    for i in range(len(ciag)):
        for j in range(i, len(ciag)):
            tekst = ciag[i:j+1]
            if czyPalindrom(tekst) == True:
                wynik = len(tekst)
                if wynik > wynik_max:
                    wynik_max = wynik
                    tekst_max = tekst

    return tekst_max

print(najdluzszyPalindrom(t))