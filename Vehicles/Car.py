from Vehicles.Vehicle import VehicleClass

class Car (VehicleClass):
    numberOfDoors = 4

    def __init__(self):
        super().__init__()

    def Ring(self, useDefault=False):
        if useDefault:
            return super().Ring()
        else:
            print("HONK")