# Models


class Vehicle:
    def __init__(self, name, cc, license_plate, vehicle_type):
        self.name = name
        self.cc = cc
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type


class Motorcycle(Vehicle):
    def __init__(self, name, cc, license_plate, transmission):
        super().__init__(name, cc, license_plate, vehicle_type="Motorcycle")
        self.transmission = transmission
        self._mileage = 0
        self._last_oil_mileage = 0
        self._oil_change_interval = 2000
        self._last_maintenance_mileage = 0
        self.maintenance_interval = 5000


class Car(Vehicle):
    def __init__(self, name, cc, license_plate, transmission):
        super().__init__(name, cc, license_plate, vehicle_type="Car")
        self.transmission = transmission
        self._mileage = 0
        self._last_oil_mileage = 0
        self._oil_change_interval = 5000
        self._last_maintenance_mileage = 0
        self.maintenance_interval = 10000


class Garage:
    def __init__(self):
        self.gid = 1
        self._vehicles = {}
        self.capacity = 5

    def find_vehicle(self, id):
        return self._vehicles.get(id)

    def get_all_veh(self):
        if not self._vehicles:
            raise ValueError("You don't have any vehicles in your garage.")
        return list(self._vehicles.values())

    def add_vehicle(self, new_vehicle):
        if len(self._vehicles) >= self.capacity:
            raise RuntimeError("You don't have any more slots in the garage.")
        new_vehicle.id = self.gid
        self._vehicles[new_vehicle.id] = new_vehicle
        self.gid += 1

    def remove_vehicle(self, id):
        if id not in self._vehicles:
            raise KeyError(f"Vehicle with ID {id} could not be found.")
        del self._vehicles[id]
