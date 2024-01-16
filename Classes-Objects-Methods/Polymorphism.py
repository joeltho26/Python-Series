class Vehicle:
    def __init__(self,brand,year,color):
        self.brand = brand
        self.year = year
        self.color = color
        
class Car(Vehicle):
    def details(self):
        print(f"The car of {self.brand} brand is painted in {self.color} and manufactured in {self.year}.")
        
class Boat(Vehicle):
    def details(self):
        print(f"The boat of {self.brand} brand is painted in {self.color} and manufactured in {self.year}.")
        
class Airplane(Vehicle):
    def details(self):
        print(f"The airplane of {self.brand} brand is painted in {self.color} and manufactured in {self.year}.")
        
class Bicycle(Vehicle):
    def __init__(self,brand,year,color,auto):
        super().__init__(brand,year,color)
        self.auto = auto
        
    def details(self):
        print(f"The bicycle of {self.brand} brand is painted in {self.color} and manufactured in {self.year}. The bicycle has {self.auto}")
        
if __name__ == '__main__':
    car = Car("Benz",2021,'Black')
    boat = Boat("BMW",2020,'Grey')
    airplane = Airplane("Boeing",2018,'White')
    bicycle = Bicycle("Boeing",2014,'Red','no gears')
    
    for vehicle in [car,boat,airplane,bicycle]:
        vehicle.details()