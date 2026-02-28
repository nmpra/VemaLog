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

    def mileage_update(self, new_mileage):
        self._prev_mileage = self._mileage
        if new_mileage < self._mileage:
            raise ValueError("The new mileage cannot be less than the old mileage!")
        self._mileage = new_mileage
        return self._prev_mileage, self._mileage

    def oil_update(self):
        self._last_oil_mileage = self._mileage
        return self._last_oil_mileage

    def oil_status(self):
        if (self._mileage - self._last_oil_mileage) >= self._oil_change_interval:
            return False
        else:
            remaining_mileage = self._oil_change_interval - (
                self._mileage - self._last_oil_mileage
            )
            return True, remaining_mileage

    def maintenance_update(self):
        self._last_maintenance_mileage = self._mileage
        return self._last_maintenance_mileage

    def maintenance_status(self):
        if (
            self._mileage - self._last_maintenance_mileage
        ) >= self.maintenance_interval:
            return False
        else:
            remaining_mileage = self.maintenance_interval - (
                self._mileage - self._last_maintenance_mileage
            )
            return True, remaining_mileage


class Garage:
    def __init__(self):
        self.gid = 1
        self._vehicle_list = []
        self.capacity = 5

    def find_vehicle(self, id):
        for k in self._vehicle_list:
            if k.id == id:
                return k
        return None

    def get_all_veh(self):
        if not self._vehicle_list:
            raise ValueError("You don't have any vehicles in your garage.")
        return self._vehicle_list

    def add_vehicle(self, new_vehicle):
        if len(self._vehicle_list) >= self.capacity:
            raise RuntimeError("You don't have any more slots in the garage.")
        new_vehicle.id = self.gid
        self._vehicle_list.append(new_vehicle)
        self.gid += 1

    def remove_vehicle(self, id):
        target = self.find_vehicle(id)
        if not target:
            raise KeyError(f"Vehicle with ID {id} could not be found.")
        self._vehicle_list.remove(target)
