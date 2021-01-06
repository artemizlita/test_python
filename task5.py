l = []
with open('input.txt') as f:
    s = f.read()
    l = s.split('\n')
d = {}
classes = [0 for i in range(12)]
for i in l:
    clas = int(i.split('\t')[0])
    rost = int(i.split('\t')[2])
    if clas not in d:
        d[clas] = rost
    else:
        d[clas] += rost
    classes[clas] += 1
for i in d:
    d[i] /= classes[i]
for i in range(12):
    print(i, end = ' ')
    if i in d:
        print(d[i])
    else:
        print('-')
