a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for elema in a:
    for elemb in b:
        if elemb == elema:
           c.append(elemb)
d = []
for x in c:
   if x not in d:
        d.append(x)
print(d)



