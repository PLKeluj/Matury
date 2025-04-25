plik = open("pi_przyklad.txt")
linie = plik.readlines()

for i in range(len(linie)):
    linie[i] = int(linie[i].rstrip())

fragmentyDwucyfrowe = []
for i in range(len(linie) - 1):
    fragmentyDwucyfrowe.append(str(linie[i]) + str(linie[i + 1]))
    ile = 0
    for fragment in fragmentyDwucyfrowe:
        if int(fragment) > 90:
            ile += 1

print(ile)