plik = open("pi_przyklad.txt")
linie = plik.readlines()

for i in range(len(linie)):
    linie[i] = int(linie[i].rstrip())

fragmentyDwucyfrowe = {}
x = 0
for x in range(100):
    fragmentyDwucyfrowe[(int(str(linie[x]) + str(linie[x + 1])))] = 0

for i in range(len(linie) - 1):
        fragmentyDwucyfrowe[int(str(linie[i]) + str(linie[i + 1]))] = fragmentyDwucyfrowe.get(
            int(str(linie[i]) + str(linie[i + 1]))) + 1

print(max(fragmentyDwucyfrowe, key=fragmentyDwucyfrowe.get),
      fragmentyDwucyfrowe.get(max(fragmentyDwucyfrowe, key=fragmentyDwucyfrowe.get)))
print(min(fragmentyDwucyfrowe, key=fragmentyDwucyfrowe.get),
      fragmentyDwucyfrowe.get(min(fragmentyDwucyfrowe, key=fragmentyDwucyfrowe.get)))
