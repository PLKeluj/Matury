n = 1000000
sito = [0] * n

sito[0] = False
sito[1] = False
for h in range(2, n):
    sito[h] = True
for i in range(1, n):
    if sito[i - 1]:
        j = i * i
        while j <= n:
            sito[j - 1] = False
            j = j + i

print(sito)

# j = i * i
# [0, False, True, True, True, True, True, True, False, True, True, False, True, True, False, False, True, False, True, False]
# j = i * 2
# [0, False, True, True, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False]
