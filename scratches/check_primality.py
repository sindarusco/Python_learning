def get_integer(help_text):
    return int(input(help_text))
def get_remainder(x, y):
    return int(x % y)

# number = get_integer('please input a number:')
#print(number)
number = 2^32 + 1

i = 2
while i < number:
    if get_remainder(number,i) == 0:
        print('this is not a prime number')
        break
    if get_remainder(number,i) != 0:
        i = i + 1
while i >= number:
    print('this is a prime number')
    break




    #remainder = get_remainder(number,i)

  #  print(remainder)

        #print('this is a prime number')











