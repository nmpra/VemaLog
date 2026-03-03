# Service


class MaintenanceLogic:

    @staticmethod
    def mileage_update(vehicle, new_mileage):
        vehicle._prev_mileage = vehicle._mileage
        if new_mileage < vehicle._mileage:
            raise ValueError("The new mileage cannot be less than the old mileage!")
        vehicle._mileage = new_mileage
        return vehicle._prev_mileage, vehicle._mileage

    @staticmethod
    def oil_update(vehicle):
        vehicle._last_oil_mileage = vehicle._mileage
        return vehicle._last_oil_mileage

    @staticmethod
    def oil_status(vehicle):
        if (
            vehicle._mileage - vehicle._last_oil_mileage
        ) >= vehicle._oil_change_interval:
            return False, None
        else:
            remaining_mileage = vehicle._oil_change_interval - (
                vehicle._mileage - vehicle._last_oil_mileage
            )
            return True, remaining_mileage

    @staticmethod
    def maintenance_update(vehicle):
        vehicle._last_maintenance_mileage = vehicle._mileage
        return vehicle._last_maintenance_mileage

    @staticmethod
    def maintenance_status(vehicle):
        if (
            vehicle._mileage - vehicle._last_maintenance_mileage
        ) >= vehicle.maintenance_interval:
            return False, None
        else:
            remaining_mileage = vehicle.maintenance_interval - (
                vehicle._mileage - vehicle._last_maintenance_mileage
            )
            return True, remaining_mileage
