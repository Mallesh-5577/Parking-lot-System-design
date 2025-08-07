from vehicle_type import VehicleType

class Vehicle:
    def __init__(self, license_plate: str):
        self.license_plate = license_plate

    def get_type(self):
        raise NotImplementedError

class Car(Vehicle):
    def get_type(self):
        return VehicleType.CAR

class Motorcycle(Vehicle):
    def get_type(self):
        return VehicleType.MOTORCYCLE

class Truck(Vehicle):
    def get_type(self):
        return VehicleType.TRUCK
