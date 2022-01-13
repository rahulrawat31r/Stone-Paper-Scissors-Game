import random
i = 5
while(i>0):
    print("\nYour turn: \nType (s) for stone, (p) for paper, (t) for scissors--->")
    a = input("Enter your choice: ")
    print("Computer turn")
    ra = random.randint(1,3)
    if (ra==1):
        b = "s"
        c = "Stone"
    elif (ra==2):
        b = "p"
        c = "Paper"
    else:
        b = "t"
        c = "Scissors"
    if (a=="s"):
        if (b=="s"):
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nIts a tie")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
        elif (b=="p"):
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nSorry you loose the game")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
        else:
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nCongragulations you won the game!")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
    elif a=="p":
        if (b=="s"):
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nCongragulations you won the game!")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
        elif (b=="p"):
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nIts a tie")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
        else:
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nSorry you loose the game")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
    else:
        if (b=="s"):
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nSorry you loose the game")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
        elif (b=="p"):
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nCongragulations you won the game")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
        else:
            print(f"computer choose {c}")
            print("And the result is .......")
            print("\nIts a tie")
            d = input("Do you want to play again? (y/n): ")
            if (d=="y"):
                continue
            else:
                break
       