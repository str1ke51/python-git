import random

winMessage = "You win!"
lostMessage = "Computer wins!"
tieMessage = "It's a tie!"

choice = -1

while choice != 0:
    choice = input("wybierz figure: [1]kamień, [2]papier, [3]nożyce")
    choice = int(choice)
    
    computerChoice = random.randint(1,3)
    print("computerChoice: " + str(computerChoice))

    if choice == 0:
        break

    if choice == computerChoice:
        print(tieMessage)
        continue

    if choice == 1:
        if computerChoice == 2:
            print (lostMessage)
        else:
            print (winMessage)

    elif choice == 2:
        if computerChoice == 3:
            print(lostMessage)
        else:
            print(winMessage)

    elif choice == 3:
        if computerChoice == 1:
            print(lostMessage)
        else:
            print(winMessage)