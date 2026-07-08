from abc import abstractmethod,ABC

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def display(self):
        pass

class Bike(vehicle):
    def start(self):
        print("starting Bike")

Bike=Bike()
Bike.start()
