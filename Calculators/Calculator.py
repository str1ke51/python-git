# Klasa opisująca kalkulator
class Calculator:
    memory = 0

    def __init__(self, initMemory):
        self.memory = initMemory

    # Operacje matematyczne
    def Add(self, number1, number2):
        return number1 + number2

    def Subtract(self, number1, number2):
        return number1 - number2


    # Zarządzanie pamięcią
    def MemPlus(self, number):
        self.memory += number
    
    def MemMinus(self, number):
        self.memory -= number

    def MemCheck(self):
        return self.memory

    def PrintMem(self):
        print(self.memory)

    # KONIEC KLASY


naszKalkulator = Calculator(3)
naszKalkulator2 = Calculator(5)
#naszKalkulator.PrintMem()

result = naszKalkulator.Add(4, 6)
naszKalkulator.MemPlus(result)

naszKalkulator.PrintMem()
naszKalkulator2.PrintMem()

#result = naszKalkulator.Subtract(4, 6)
#naszKalkulator.MemMinus(result)

#naszKalkulator.PrintMem()