num = input("gimme a number ")
num = int(num)
for i in range(1, num):
    ls=[]
    if num % i == 0:
        ls.append(i)
        for item in ls:
            print(item)

