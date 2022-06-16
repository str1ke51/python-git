# Definicja funkcji
def WelcomeUser():
    print("- - - - - - - - POCZATEK PROGRAMU - - - - - - - -")

    # Przyjęcie danych
    fn = input("What is your first name? ")
    ln = input("What is your last name? ")
    age = input("How old are you? ")
    age = int(age)
    return fn, ln, age


def Add(number1, number2):
    result = number1 + number2
    print(str(number1) + " + " + str(number2) + " = " + str(result))
    return result


# 5! = 1 * 2 * 3 * 4 * 5    = 4! * 5
# 4! = 1 * 2 * 3 * 4        = 3! * 4
# 3! = 1 * 2 * 3            = 2! * 3
# ...
# 1! = 1
def Factorial(number):
    if number == 1:
        return 1

    return Factorial(number - 1) * number


# Wywołanie funkcji
firstName, lastName, age = WelcomeUser()
print(firstName, lastName, age)

# Definicje zmiennych
numberOne = 30.2
numberTwo = 2
ageLimit = 18

print( Add(numberOne, numberTwo) )

#welcome = "Hi!\nMy name is " + firstName + " " + lastName + ".\nI'm " + str(age) + " years old."
#print(welcome)

# Sprawdzenie pełnoletności
isUnderage = age < ageLimit #typ: bool
if not isUnderage and not firstName.endswith("a"):
    #print("I'm over 18 years old.")
    print("Jestem pełnoletni.")
elif not isUnderage:
    print("Jestem pełnoletnia.")
else:
    print("I'm underage.")


# Policzenie silni z podanego wieku
ageFactorial = Factorial(age)
print(str(age) + "! = " + str(ageFactorial))


"""
for i in range(10):
    if i == 1:
        print(str(i) + " - jedynka")
    elif i % 2 == 0:
        print(str(i) + " - parzysta")
    else:
        print(str(i) + " - nieparzysta")
"""