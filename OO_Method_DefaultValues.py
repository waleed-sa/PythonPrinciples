class Truck:
    '''-> Truck - a type of automobile. '''

    def dumpload(self, value=None):
        if value is None:
            print("Truck has nothing to dump")
        else:
            print("Truck is dumping " + str(value))

myTruck = Truck()
myTruck.dumpload(5)


    

    
