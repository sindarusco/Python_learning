number = input("what is your number? ")
number = int(number)
divider = input("what is your divider ")
divider = int(divider)
if number % divider == 0:
    print("even")
# if number % 4 == 0:
#     print("even even")
if number % divider != 0:
    print("odd")
