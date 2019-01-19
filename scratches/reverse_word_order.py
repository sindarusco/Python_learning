originalstring = input("please input a string:")
iteminstring = originalstring.split(" ")
print(iteminstring)
L = len(iteminstring)
# print(L)
for i in range(L):
    j = L - 1 - i
    # print(i)
    newstring = [None] * L
    newstring[j] = iteminstring[i]
print(newstring)
    # print(j)
    # print(i)
    # print(j)



