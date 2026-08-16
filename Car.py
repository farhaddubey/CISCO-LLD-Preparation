
class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount

        if self.speed < 0:
            self.speed = 0

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed}")

class Car(Vehicle):

    def __init__(brand, model, number_of_doors):
        super.__init__(brand, model)

        self.number_of_doors = number_of_doors

class Bike(Vehicle):

    def __init__(self, brand, model, has_carrier):
        super().__init__(brand, model)

        self.has_carrier = has_carrier

    def display_info(self):
        # Parent executes it's own version 
        super().display_info()

        # Then I'll add my own behaviour
        print(f"Carrier: {self.has_carrier}")