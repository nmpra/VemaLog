from fastapi import FastAPI, HTTPException
from models import Motorcycle, Car, Garage
from service import MaintenanceLogic

app = FastAPI()
my_garage = Garage()


def dummy_data(my_garage):
    m1 = Motorcycle("Vario 160 eSP+", 160, "H 1234 ABC", "Automatic")
    m2 = Motorcycle("ZX-25RR", 250, "B 3344 SSS", "Manual")
    m3 = Motorcycle("WR155R", 155, "K 9901 ZZ", "Manual")
    c1 = Car("Innova Venturer", 2400, "AD 1 ABC", "Automatic")

    my_garage.add_vehicle(m1)
    my_garage.add_vehicle(m2)
    my_garage.add_vehicle(m3)
    my_garage.add_vehicle(c1)


dummy_data(my_garage)


@app.get("/vehicles")
def get_all_vehicles():
    vehicles = [v.__dict__ for v in my_garage.get_all_veh()]
    return {"vehicles": vehicles}


@app.get("/vehicles/{id}")
def get_vehicles_id(id: int):
    vehicles = my_garage.find_vehicle(id)
    if vehicles is None:
        raise HTTPException(
            status_code=404, detail=f"Vehicle with ID {id} could not be found."
        )
    return {"vehicle": vehicles}


@app.delete("/vehicles/{id}")
def remove_vehicles(id: int):
    try:
        my_garage.remove_vehicle(id)
        return {
            f"message": f"Vehicle with ID {id} has been removed.",
            "status": "success",
        }
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Vehicle with ID {id} could not be found."
        )
