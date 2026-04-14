plik = open('zegar_binarny.txt')
zegary = []
for i in plik:
    zegary.append((i.strip()).split())

wiersze = []
for i in range(len(zegary)):
    if int(zegary[i][0],2) == 1 and int(zegary[i][1],2) == 7 and int(zegary[i][2],2) == 2 and int(zegary[i][3],2) == 2 and int(zegary[i][4],2) == 1 and int(zegary[i][5],2) == 4:
        wiersze.append(i+1)

print(len(wiersze))
print(wiersze)