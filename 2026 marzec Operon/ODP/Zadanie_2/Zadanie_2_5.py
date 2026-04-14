plik = open('zegar_binarny.txt')
zegary = []
for i in plik:
    zegary.append((i.strip()).split())

wynik = []
for i in range(len(zegary)):
    m_1 = int(zegary[i][2],2)
    m_2 = int(zegary[i][3], 2)
    minuta = m_1*10 + m_2

    s_1 = int(zegary[i][4], 2)
    s_2 = int(zegary[i][5], 2)
    sekunda = s_1*10 + s_2

    if minuta == sekunda:
        wynik.append(zegary[i])

print(wynik)