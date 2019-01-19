name = input("your name? ")
age = input("your age? ")
age = int(age)
copies = input("how many copies do you want? ")
copies = int(copies)
current_year = 2018
current_year = int(current_year)
target_age = 100
target_age = int(target_age)
year_of_100 = target_age - age + current_year
for i in range(copies):
    print("your name is " + name)
    print("your age is " + str(age))
    print("you will be 100 years old at " + str(year_of_100) + "\n")

