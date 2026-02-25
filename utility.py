# Utility


def input_string(pesan, min_len=0):
    while True:
        data = input(pesan).strip()
        if not data:
            print("Input tidak boleh KOSONG.")
            continue
        if len(data) < min_len:
            print(f"Input terlalu pendek, minimal {min_len} karakter.")
            continue
        return data


def input_angka(pesan, min_len=0):
    while True:
        data = input(pesan).strip()
        if not data:
            print("Input tidak boleh KOSONG.")
            continue
        if len(data) < min_len:
            print(f"Input terlalu pendek, minimal {min_len} karakter.")
            continue
        try:
            return int(data)
        except ValueError:
            print("Input harus berupa ANGKA.")


def input_choice(pesan, choices):
    while True:
        data = input(pesan).capitalize()
        if data in choices:
            return data
        print(f"Input salah, input harus berupa salah satu dari: {', '.join(choices)}")
        continue


def vehicle_table(vehicle_list):
    if not vehicle_list:
        print("There is no vehicle in the garage.")
        return

    print("\n" + "=" * 65)
    print(f"{"GARASI":^65}")
    print("=" * 65)

    for k in vehicle_list:
        print(
            f"| {str(k.id):<3} | {k.nama:<20} | {str(k.cc):<5}cc | {k.plat:<12} | {k._odometer:<7}km |"
        )

    print("=" * 65)
