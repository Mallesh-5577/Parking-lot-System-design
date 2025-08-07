from threading import Lock

class ParkingLot:
    _instance = None
    _lock = Lock()

    def __init__(self, levels: list):
        self.levels = levels

    @classmethod
    def get_instance(cls, levels=None):
        with cls._lock:
            if not cls._instance:
                if levels is None:
                    raise ValueError("First initialization requires levels.")
                cls._instance = ParkingLot(levels)
            return cls._instance

    def park_vehicle(self, vehicle):
        for level in self.levels:
            spot = level.park_vehicle(vehicle)
            if spot:
                return (level.level_id, spot.spot_id)
        return None

    def remove_vehicle(self, license_plate: str):
        for level in self.levels:
            if level.remove_vehicle(license_plate):
                return True
        return False

    def get_available_spots(self):
        return [(l.level_id, l.get_available_spots()) for l in self.levels]
