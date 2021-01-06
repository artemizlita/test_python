s = int(input())
lst = [[0 for i in range(s)] for j in range(s)]
k = 1
s -= 1
r = s
d = s
while r >= 0:
    for i in range(d + 1):
        lst[s - r][i + s - r] = k
        k += 1
    for i in range(d):
        lst[i + 1 + s - r][r] = k
        k += 1
    for i in range(d):
        lst[r][r - i - 1] = k
        k += 1
    for i in range(d - 1):
        lst[r - i - 1][s - r] = k
        k += 1
    r -= 1
    d -= 2
for i in range(s + 1):
    for j in range(s + 1):
        print(lst[i][j], end = ' ')
    print()
