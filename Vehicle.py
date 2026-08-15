
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
        print(f "Brand : {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed}")