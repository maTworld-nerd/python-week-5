# Base class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        return f"{self.brand} {self.model}'s engine starts with a roar!"

    def stop_engine(self):
        return f"{self.brand} {self.model}'s engine shuts down quietly."

# Derived class (Inheritance)
class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity  # Unique attribute
    
    def start_engine(self):
        return f"{self.brand} {self.model}'s engine starts silently with electric power!"
    
    def charge_battery(self):
        return f"{self.brand} {self.model} is charging. Battery capacity: {self.battery_capacity} kWh."

# Testing the class
tesla = ElectricCar("Tesla", "Model S", 2023, 100)
toyota = Vehicle("Toyota", "Camry", 2021)

print(tesla.start_engine())
print(tesla.charge_battery())
print(toyota.start_engine())
print(toyota.stop_engine())
