import random

time = 1
randx = random.randint(1, 9)
while time > 0:
    x = input("your guess?\n")
    try:
        val = int(x) and int(x) < 9
    except ValueError:
        x = input("your guess?\n")
    if int(x) > randx:
        print("too big")
        time = time + 1
    elif int(x) < randx:
        print("too small")
        time = time + 1
    elif int(x) == randx:
        print("good guess")
        print(str(time) + " guesses")
        y = input("next round! Y/N\n")
        if y == "Y" or "y":
            time = 1
            randx = random.randint(1, 9)
        else:
            exit()



