shif = input()
rash = input()
ds = {}
for i in range(len(shif)):
    ds[shif[i]] = rash[i]
de = {}
for i in range(len(rash)):
    de[rash[i]] = shif[i]
s1 = input()
s2 = input()
s1_new = ''
s2_new = ''
for i in range(len(s1)):
    s1_new += ds[s1[i]]
for i in range(len(s2)):
    s2_new += de[s2[i]]
print(s1_new)
print(s2_new)
