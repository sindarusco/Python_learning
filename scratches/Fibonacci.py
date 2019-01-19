def fibonacci(n):
    n0 = 0
    n1 = 1
    count = 0

    if n <= 0:
        print ('please input a positive integer')
    if n == 1:
        print(n0)
    if n >= 2:
        while count < n:
            print(n0, end= ', ')
            nth = n0 + n1
            n0 = n1
            n1 = nth
            count = count + 1


n = input('how many terms do you want? ')
n = int(n)
fibonacci(n)