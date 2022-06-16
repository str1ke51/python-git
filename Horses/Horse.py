# Klasa opisująca konia
class Horse:
    name = ""
    age = 20
    favouriteNumber = 0

    def __init__(self):
        pass

    def __str__(self) -> str:
        return "Hi! I'm " + self.name + ", I'm a horse and my fav number is " + str(self.favouriteNumber) + "!"

    def Count(self):
        for x in range(self.favouriteNumber):
            print(x)

    def Drink(self):
        if self.age > 18:
            print("I'm drinking :)")
        else:
            raise Exception("I'm underage :(")