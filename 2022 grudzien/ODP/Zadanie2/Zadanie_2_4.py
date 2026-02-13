plik = open('pary.txt')
liczby = []
for i in plik:
    a, b = (i.strip()).split()
    liczby.append([int(a),int(b)])

for i in liczby:
    a, b = i[0], i[1]
    t = b
    while t > a:
        t = t//2
        if t == a:
            print(a, b)