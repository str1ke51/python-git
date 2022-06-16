from Vehicles.Vehicle import VehicleClass
from Vehicles.Car import Car
from Vehicles.Tram import Tram

# Lista moich pojazdów
myVehicleList = []

myCar = Car()
myTram = Tram()

myVehicleList.append(myCar)
myVehicleList.append(myTram)
myVehicleList.append(myTram)
myVehicleList.append(myCar)
myVehicleList.append(myTram)

for vehicle in myVehicleList:
    if type(vehicle) is Car:
        vehicle.Ring()

    if type(vehicle) is Tram:
        vehicle.PantographDown()

    vehicle.Go()