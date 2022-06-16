class VehicleClass:
    numberOfWheels = 4
    isGoing = False

    def __init__(self):
        pass

    def Ring(self):
        print("Ringing...")

    def Go(self):
        if self.isGoing:
            print("Already going...")
        else:
            print("Going...")

    def Stop(self):
        if self.isGoing:
            print("Stopping...")
        else:
            print("Already stopped...")
