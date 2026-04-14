plik = open('dane8.txt', 'r')

liczby = []
for i in plik:
    liczby.append(int(i.strip()))

# liczby = [2, 4, 10, 6, 8, 1, 3, 7, 9, 5]
dl = [1] * len(liczby)

for i in range(1, len(liczby)):
    max_index = 0
    for j in range(i-1, 0, -1):
        if liczby[i] > liczby[j] and dl[j] >= dl[max_index]:
            max_index = j
    if liczby[i] > liczby[max_index]:
        dl[i] += dl[max_index]

print(max(dl))
