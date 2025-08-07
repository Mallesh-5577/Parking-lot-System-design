from threading import Lock

class Level:
    def __init__(self, level_id: int, spots: list):
        self.level_id = level_id
        self.spots = spots
        self.lock = Lock()

    def park_vehicle(self, vehicle):
        with self.lock:
            for spot in self.spots:
                if spot.can_fit_vehicle(vehicle):
                    spot.assign_vehicle(vehicle)
                    return spot
            return None

    def remove_vehicle(self, license_plate: str):
        with self.lock:
            for spot in self.spots:
                if spot.vehicle and spot.vehicle.license_plate == license_plate:
                    spot.remove_vehicle()
                    return True
            return False

    def get_available_spots(self):
        with self.lock:
            return sum(1 for spot in self.spots if spot.is_available())
