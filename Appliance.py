class Appliance: 

    def __init__(self, brand, power):
        self.brand = brand
        self.power = power 

    def calculate_power_consumption(self, hours):
        return self.power * hours

class WashineMachine(Appliance):

    def __init__(self, brand, power, hours):
        super.__init__(brand, power)

        self.hours = hours

        s
class AirConditioner(Appliance):