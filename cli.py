# Command Line Interface

import os
import utility as u
from models import Motorcycle, Car
from service import MaintenanceLogic as m


def dummy_data(my_garage):
    m1 = Motorcycle("Vario 160 eSP+", 160, "H 1234 ABC", "Automatic")
    m2 = Motorcycle("ZX-25RR", 250, "B 3344 SSS", "Manual")
    m3 = Motorcycle("WR155R", 155, "K 9901 ZZ", "Manual")
    c1 = Car("Innova Venturer", 2400, "AD 1 ABC", "Automatic")

    my_garage.add_vehicle(m1)
    my_garage.add_vehicle(m2)
    my_garage.add_vehicle(m3)
    my_garage.add_vehicle(c1)

    print("\n[SYSTEM] 4 Dummy Data Loaded Successfully.")


def vehicle_list(my_garage):
    os.system("cls")
    Garage = my_garage.get_all_veh()
    u.vehicle_table(Garage)
    while True:
        print("0. Back To Main Menu,")
        print("1. Show Vehicle Detail.")
        choice = u.num_input("Input Your Choice: ")
        if choice == 0:
            break
        elif choice == 1:
            get_id = u.num_input("=== Input Vehicle ID: ")
            for v in my_garage._vehicle_list:
                if get_id == v.id:
                    print("\n" + "=" * 67)
                    print(f"{"VEHIclE DETAIL":^67}")
                    print("=" * 67)
                    print(
                        f"| {str(v.id):<3} | {v.name:<20} | {str(v.cc):<5}cc | {v.license_plate:<12} | {v._mileage:<7}km |"
                    )
                    print("=" * 67)
                    print(f"| {"Last Oil Change":<25} | {v._last_oil_mileage:<7}km |")
                    print(
                        f"| {"Last Vehicle Maintenance":<25} | {v._last_maintenance_mileage:<7}km |"
                    )
                    print("=" * 41 + "\n")
                    break
        else:
            print("Wrong input!")


def add_vehicle(my_garage):
    os.system("cls")
    while True:
        print("=== Type '0' to quit")
        vehicle_type = u.choice_input(
            "Choice Vehicle Type (Motorcycle/Car): ",
            choices=["Motorcycle", "Car", "0"],
        )

        if vehicle_type == "Motorcycle":
            name = u.text_input("Input Vehicle Name: ", min_len=3).capitalize()
            cc = u.num_input("Input Cylinder Capacity: ", min_len=2)
            license_plate = u.text_input(
                "Input License Plate Number: ", min_len=3
            ).upper()
            transmission = u.choice_input(
                "Input Transmission Type (Automatic/Manual): ",
                choices=["Automatic", "Manual"],
            )
            m = Motorcycle(name, cc, license_plate, transmission)
            my_garage.add_vehicle(m)
            print(f"\n{m.name} added successfully (ID: {m.id})\n")

        elif vehicle_type == "Car":
            name = u.text_input("Input Vehicle Name: ", min_len=3).capitalize()
            cc = u.num_input("Input Cylinder Capacity: ", min_len=3)
            license_plate = u.text_input(
                "Input License Plate Number: ", min_len=3
            ).upper()
            transmission = u.choice_input(
                "Input Transmission Type (Automatic/Manual): ",
                choices=["Automatic", "Manual"],
            )
            c = Car(name, cc, license_plate, transmission)
            my_garage.add_vehicle(c)
            print(f"\n{c.name} added successfully (ID: {c.id})\n")

        elif vehicle_type == "0":
            break


def mileage_update(my_garage):
    os.system("cls")
    while True:
        Garage = my_garage.get_all_veh()
        u.vehicle_table(Garage)
        get_id = u.num_input("Input Vehicle ID (0 To Quit): ")
        if get_id == 0:
            print("\nUpdate cancelled, return to main menu...")
            break
        for v in my_garage._vehicle_list:
            if get_id == v.id:
                new_mileage = u.num_input("Input New Vehicle Mileage: ")
                m.mileage_update(v, new_mileage)
                print("\nMileage Updated.")
                print(f"Mileage: {v._prev_mileage}km => {v._mileage}km")
                break
        else:
            print(f"Vehicle with ID {get_id} not found.")


def vehicle_status(my_garage):
    os.system("cls")
    while True:
        Garage = my_garage.get_all_veh()
        u.vehicle_table(Garage)
        get_id = u.num_input("Input Vehicle ID (0 To Quit): ")
        if get_id == 0:
            print("\nUpdate cancelled, return to main menu...")
            break
        for v in my_garage._vehicle_list:
            if get_id == v.id:
                status, mileage = m.oil_status(v)
                if not status:
                    print(
                        f"Warning! Oil change required. Overdue by {v._mileage - v._last_oil_mileage} km."
                    )
                else:
                    print(
                        f"Status: Safe. {mileage} km remaining until next oil change."
                    )
                status, mileage = m.maintenance_status(v)
                if not status:
                    print(
                        f"Warning! Maintenance required. Overdue by {v._mileage - v._last_maintenance_mileage} km."
                    )
                else:
                    print(
                        f"Status: Safe. {mileage} km remaining until next maintenance."
                    )
                break
        else:
            print(f"Vehicle with ID {get_id} not found.")


def status_update(my_garage):
    os.system("cls")
    while True:
        Garage = my_garage.get_all_veh()
        u.vehicle_table(Garage)
        print("\n1. Update Vehicle Oil Change Mileage.")
        print("2. Update Vehicle Maintenance Mileage.")
        choice = u.num_input("Input Your Choice (0 To Quit): ")

        if choice == 1:
            get_id = u.num_input("=== Input Vehicle ID: ")
            for v in my_garage._vehicle_list:
                if get_id == v.id:
                    m.oil_update(v)
                    print("Oil Change Mileage Successfully Updated.")
                    print(f"Current Mileage: {v._last_oil_mileage}km")
                    break
            else:
                print(f"Vehicle with ID {get_id} not found.")

        elif choice == 2:
            get_id = u.num_input("=== Input Vehicle ID: ")
            for v in my_garage._vehicle_list:
                if get_id == v.id:
                    m.maintenance_update(v)
                    print("Maintenance Mileage Successfully Updated.")
                    print(f"Current Mileage: {v._last_oil_mileage}km")
                    break
            else:
                print(f"Vehicle with ID {get_id} not found.")

        elif choice == 0:
            break

        else:
            print("Wrong Input. Please Choice The Right Input Choises!")


def remove_vehicle(my_garage):
    os.system("cls")
    while True:
        Garage = my_garage.get_all_veh()
        u.vehicle_table(Garage)
        get_id = u.num_input("Input Vehicle ID (0 To Quit): ")
        if get_id == 0:
            print("\nUpdate cancelled, return to main menu...")
            break
        for v in my_garage._vehicle_list:
            if get_id == v.id:
                validation = u.choice_input(
                    "Are You Sure You Want To Remove This Vehicle (Y/N): ",
                    choices=["Y", "N"],
                )
                if validation == "Y":
                    my_garage.remove_vehicle(get_id)
                    print(f"Vehicle with ID {get_id} has been removed.")
                    break
                elif validation == "N":
                    print("Update Cancelled, return to main menu...")
                    break
        else:
            print(f"Vehicle with ID {get_id} not found.")


def run_cli(my_garage):
    dummy_data(my_garage)

    while True:

        try:
            print("\n" + "=" * 40)
            print(f"{"VEHICLE MAINTENANCE LOG":^40}")
            print("=" * 40)
            print("1. Show Vehicles In Garage")
            print("2. Add New Vehicles")
            print("3. Update Vehicle Mileage")
            print("4. Show Vehicles Status")
            print("5. Update Vehicle Status")
            print("6. Remove Vehicles")
            print("0. Close Program")
            print("=" * 40)

            pilihan = input("Choice Menu (0-6): ")

            if pilihan == "1":
                vehicle_list(my_garage)

            elif pilihan == "2":
                add_vehicle(my_garage)

            elif pilihan == "3":
                mileage_update(my_garage)

            elif pilihan == "4":
                vehicle_status(my_garage)

            elif pilihan == "5":
                status_update(my_garage)

            elif pilihan == "6":
                remove_vehicle(my_garage)

            elif pilihan == "0":
                print("\nProgram closed.")
                break

            else:
                print("\nInvalid choice.")

        except Exception as e:
            print(f"\nError! Message: {e}")
