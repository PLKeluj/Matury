slowo = 'samochod'


def szyfrPrzestawienny(slowo):
    szyfrogram = ''
    for i in range(0, len(slowo), 2):
        szyfrogram += slowo[i + 1]
        szyfrogram += slowo[i]
    return szyfrogram


szyfr = 'asomhcdo'


def deszyfrPrzestawienny(szyfr):
    slowo = ''
    for i in range(0, len(szyfr), 2):
        slowo += szyfr[i + 1]
        slowo += szyfr[i]
    return slowo
