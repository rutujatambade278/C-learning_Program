from abc import ABC, abstractmethod

# Interface 1
class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass

# Interface 2
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

# Class implementing multiple interfaces
class FlyingCar(Drivable, Flyable):
    def drive(self):
        return "Driving on the road"

    def fly(self):
        return "Flying in the sky"

# Creating an object of the class
flying_car = FlyingCar()
print(flying_car.drive())  # Output: Driving on the road
print(flying_car.fly())    # Output: Flying in the sky
