n = int(input())
d = {}
for i in range(n):
    s = input()
    l = s.split(';')
    if l[0] not in d:
        d[l[0]] = [0, 0, 0, 0, 0]
    d.get(l[0])[0] += 1
    if l[2] not in d:
        d[l[2]] = [0, 0, 0, 0, 0]
    d.get(l[2])[0] += 1
    if int(l[1]) > int(l[3]):
        d.get(l[0])[1] += 1
        d.get(l[2])[3] += 1
        d.get(l[0])[4] += 3
    elif int(l[1]) == int(l[3]):
        d.get(l[0])[2] += 1
        d.get(l[2])[2] += 1
        d.get(l[0])[4] += 1
        d.get(l[2])[4] += 1
    else:
        d.get(l[2])[1] += 1
        d.get(l[0])[3] += 1
        d.get(l[2])[4] += 3
for i in d:
    print(i + ':' + str(d.get(i)[0]), str(d.get(i)[1]), str(d.get(i)[2]), str(d.get(i)[3]), str(d.get(i)[4]))
