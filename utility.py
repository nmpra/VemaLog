# Utility


def text_input(message, min_len=0):
    while True:
        data = input(message).strip()
        if not data:
            print("Input cannot be empty.")
            continue
        if len(data) < min_len:
            print(f"Input too short, minimum {min_len} characters.")
            continue
        return data


def num_input(message, min_len=0):
    while True:
        data = input(message).strip()
        if not data:
            print("Input cannot be empty.")
            continue
        if len(data) < min_len:
            print(f"Input too short, minimum {min_len} characters.")
            continue
        try:
            return int(data)
        except ValueError:
            print("Input must be a number.")


def choice_input(message, choices):
    while True:
        data = input(message).capitalize()
        if data in choices:
            return data
        print(f"Invalid input, must be one of: {', '.join(choices)}")
        continue


def vehicle_table(vehicle_list):
    print("\n" + "=" * 65)
    print(f"{"GARAGE":^65}")
    print("=" * 65)

    for v in vehicle_list:
        print(
            f"| {str(v.id):<3} | {v.name:<20} | {str(v.cc):<5}cc | {v.license_plate:<12} | {v._mileage:<7}km |"
        )

    print("=" * 65)
