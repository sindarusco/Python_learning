i = 1
while i < 2:
    P_one = input("player 1 please input: ")
    while (P_one != "rock") and (P_one != "paper") and (P_one != "scissor"):
        P_one = input("player 1 please input: ")

    P_two = input("player 2 please input: ")
    while (P_two != "rock") and (P_two != "paper") and (P_two != "scissor"):
        P_two = input("player 2 please input: ")

    if P_one == P_two:
        print("draw \n")

    elif (P_one == "rock" and P_two == "scissor") or (P_one == "scissor" and P_two == "paper") or (P_one == "paper" and P_two == "rock"):
        print("player 1 win")

    elif (P_one == "rock" and P_two == "paper") or (P_one == "scissor" and P_two == "rock") or (P_one == "paper" and P_two == "scissor"):
        print("player 2 win")

    again = input("play again? Y/N \n")
    while (again != "Y") and (again != "N") and (again != "y") and (again != "n"):
        again = input("play again? Y/N \n")

    if again == "Y" or again == "y":
        continue
    else:
        print("Bye")
        break
