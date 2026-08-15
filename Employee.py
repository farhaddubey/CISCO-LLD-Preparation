
class Employee:

    def __init__(self, id, name, base_salary):
        self.id = id 
        self.name = name 
        self.base_salary = base_salary

    # Same method -> different implementtations -> Runtim Polymorphhism 
    def calculate_salary(self):
        return self.base_salary

    

class Manager(Employee):

    def __init__(self, id, name, base_salary, bonus):
        super().__init__(id, name, base_salary)
        self.bonus = bonus

    # Same method different implementations -> Runtime Polymorphism 
    def calculate_salary(self):
        return self.base_salary + self.bonus_salary

class Developer(Employee):

    def __init__(self, id, name, base_salary, overtime_hours, hourly_rate):
        super().__init__(id, name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    # Same method different implementations -> Runtime Polymorphism
    def calculate_salary(self):
        overtime_pay = (self.overtime_hours * self.hourly_rate)
        return self.base_salary + overtime_pay