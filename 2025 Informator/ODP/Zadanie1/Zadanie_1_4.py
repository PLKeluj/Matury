plik = open('dane1_4.txt', 'r')
liczby = []

for i in plik:
    liczby.append(int(i.strip()))

# liczby = [2, -3, 1, -7, 4, -2, -1, 5, -3, 2, -1]

sumy = [0] * len(liczby)

index = 0
for i in range(len(sumy), 0, -1):
    sumy[index] = [0] * i
    index += 1

for i in range(len(liczby)):
    for j in range(i, len(liczby)):
        if j == 0:
            sumy[i][j] = liczby[j]
        else:
            sumy[i][j - i] = sumy[i][j - i - 1] + liczby[j]

print(sumy)
max = 0
id_p = 0
id_k = 0

for i in range(len(sumy)):
    for j in range(len(sumy[i])):
        if sumy[i][j] > max:
            max = sumy[i][j]
            id_p = i
            id_k = i + j

print(id_p + 1, id_k + 1)
