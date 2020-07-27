
class AutoMobile:
    '''-> Automobile base / parent class'''

    model_year = "2019"

    def start(self):
        print("Automobile is starting ... vroom, vroom!")

    def turn_off(self):
        '''-> shut off auto ...'''
        print("Click, pud, pud ... thud. Vehicle is off.")


class Truck(AutoMobile):
    '''-> Truck - a type of automobile. '''

    def dumpload(self):
        print("Truck is dumping load")

myTruck = Truck()
myTruck.start()

    

    
