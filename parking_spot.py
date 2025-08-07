from vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: VehicleType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def can_fit_vehicle(self, vehicle):
        return self.vehicle is None and vehicle.get_type() == self.spot_type

    def assign_vehicle(self, vehicle):
        if self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None
