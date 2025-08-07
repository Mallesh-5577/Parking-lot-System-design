from vehicle_type import VehicleType
from vehicle import Car, Motorcycle, Truck
from parking_spot import ParkingSpot
from level import Level
from parking_lot import ParkingLot

# Build a lot: two levels, each with 3 spots (1 car, 1 motorcycle, 1 truck)
levels = []
for i in range(2):
    spots = [ParkingSpot(spot_id=0, spot_type=VehicleType.CAR),
             ParkingSpot(spot_id=1, spot_type=VehicleType.MOTORCYCLE),
             ParkingSpot(spot_id=2, spot_type=VehicleType.TRUCK)]
    levels.append(Level(level_id=i, spots=spots))
lot = ParkingLot.get_instance(levels)

v1 = Car("KA-01-AA-1111")
v2 = Motorcycle("KA-01-BB-2222")
v3 = Truck("KA-01-CC-3333")

print("Parking Car:", lot.park_vehicle(v1))
print("Parking Motorcycle:", lot.park_vehicle(v2))
print("Parking Truck:", lot.park_vehicle(v3))
print("Available spots by level:", lot.get_available_spots())

print("Removing Car:", lot.remove_vehicle("KA-01-AA-1111"))
print("Available spots by level:", lot.get_available_spots())
