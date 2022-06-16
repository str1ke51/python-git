import random

choice = -1

def GetInput():
    numberOne = input("Input first number: ")
    numberTwo = input("Input second number: ")
    numberOne = float(numberOne)
    numberTwo = float(numberTwo)
    return numberOne, numberTwo


def Add(number1, number2, number3=0):
    result = number1 + number2 + number3
    return result


def Subtract(number1, number2):
    result = number1 - number2
    return result


def Multiply(number1, number2):
    result = number1 * number2
    return result


def Divide(number1, number2) -> float | None:
    try:
        result = number1 / number2

    except ZeroDivisionError:
        return None

    else:
        return result


def Calculate(n1, n2, choice):
    if choice == 1:
        return Add(n1, n2)

    elif choice == 2:
        return Subtract(n1, n2)

    elif choice == 3:
        return Multiply(n1, n2)

    elif choice == 4:
        return Divide(n1, n2)


while choice != 0:
    choice = input("Wybierz działanie:\n[1] Dodawanie\n[2] Odejmowanie\n[3] Mnożenie\n[4] Dzielenie\n[0] Wyjdź\n")
    choice = int(choice)

    if choice == 0:
        break

    numberOne, numberTwo = GetInput()
    result = Calculate(numberOne, numberTwo, choice)
    print(result)


"""
fruits = ["apple", "banana", "pear", "orange", "strawberry"]
for fruit in fruits:
    if fruit == "banana":
        print("YELLOW")
        continue

    print(fruit)
else:
    print("All the fruits!")

for i in range(7):
    index = random.randint(0, len(fruits) - 1)
    print(fruits[index])
"""