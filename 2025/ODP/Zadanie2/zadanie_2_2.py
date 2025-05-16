symbole = []
plik = open('symbole.txt', 'r')

for i in plik:
    symbole.append(i.strip())

for i in range(1,len(symbole)-2):
    for p in range(1, len(symbole[i])-1):
        if (symbole[i-1])[p-1] == (symbole[i])[p] and (symbole[i-1])[p] == (symbole[i])[p] and (symbole[i-1])[p+1] == (symbole[i])[p] and (symbole[i])[p-1] == (symbole[i])[p] and (symbole[i])[p+1] == (symbole[i])[p] and (symbole[i+1])[p-1] == (symbole[i])[p] and (symbole[i+1])[p] == (symbole[i])[p] and (symbole[i+1])[p+1] == (symbole[i])[p]:
            print(i+1, p+1)
