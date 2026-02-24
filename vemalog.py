# Vehicle Maintenance Log Project
import os


class Kendaraan:
    def __init__(self, nama, cc, plat, jenis):
        self.id = None
        self.nama = nama
        self.cc = cc
        self.plat = plat
        self.jenis = jenis


class Motor(Kendaraan):
    def __init__(self, nama, cc, plat, kategori):
        super().__init__(nama, cc, plat, jenis="Motor")
        self.kategori = kategori
        self._oli_interval = 2000
        self._odometer = 0
        self._oli_terakhir = 0
        self._maintenance_terakhir = 0

    def update_odo(self, odo_baru):
        self._odometer_lama = self._odometer
        if odo_baru < self._odometer:
            raise ValueError("Odometer baru tidak boleh kurang dari odometer lama!")
        self._odometer = odo_baru
        return self._odometer_lama, self._odometer

    def update_oli(self):
        self._oli_terakhir = self._odometer
        return self._oli_terakhir

    def status_oli(self):
        if (self._odometer - self._oli_terakhir) >= self._oli_interval:
            return False
        else:
            jarak_oli = self._oli_interval - (self._odometer - self._oli_terakhir)
            return True, jarak_oli

    def update_maintenance(self):
        self._maintenance_terakhir = self._odometer
        return self._maintenance_terakhir

    def status_maintenance(self):
        if self.kategori == "Matic":
            interval_maintenance = 8000
            if (self._odometer - self._maintenance_terakhir) >= interval_maintenance:
                return False
            else:
                jarak_maintenance = interval_maintenance - (
                    self._odometer - self._maintenance_terakhir
                )
                return True, jarak_maintenance
        elif self.kategori in ["Manual", "Kopling"]:
            interval_maintenance = 5000
            if (self._odometer - self._maintenance_terakhir) >= interval_maintenance:
                return False
            else:
                jarak_maintenance = interval_maintenance - (
                    self._odometer - self._maintenance_terakhir
                )
                return True, jarak_maintenance


class Garasi:
    def __init__(self):
        self._gid = 1
        self._daftar_kendaraan = []

    def cari_kendaraan(self, id):
        for k in self._daftar_kendaraan:
            if k.id == id:
                return k
        return None

    def tunjukkan_kendaraan(self):
        if not self._daftar_kendaraan:
            raise ValueError("Garasi Anda Kosong.")
        return self._daftar_kendaraan

    def tambah_kendaraan(self, obj_kendaraan):
        if len(self._daftar_kendaraan) >= 3:
            raise RuntimeError("Garasi anda penuh.")

        obj_kendaraan.id = self._gid
        self._daftar_kendaraan.append(obj_kendaraan)
        self._gid += 1

    def hapus_kendaraan(self, id):
        target = self.cari_kendaraan(id)
        if target is None:
            raise KeyError(f"Kendaraan dengan ID {id} tidak ditemukan.")
        self._daftar_kendaraan.remove(target)


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


def vehicle_tabble(vehicle_list):
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


def data_dummy(garasi):
    motor1 = Motor("Vario 160 eSP+", 160, "H 1234 ABC", "Matic")
    motor2 = Motor("ZX-25RR", 250, "B 3344 SSS", "Kopling")
    motor3 = Motor("WR155R", 155, "K 9901 ZZ", "Kopling")

    garasi.tambah_kendaraan(motor1)
    garasi.tambah_kendaraan(motor2)
    garasi.tambah_kendaraan(motor3)

    print("\n[SYSTEM] 3 Data dummy berhasil di-load.")


def main():
    my_garage = Garasi()
    data_dummy(my_garage)

    while True:

        try:
            print("\n" + "=" * 40)
            print("      VEHICLE MAINTENANCE TRACKER")
            print("=" * 40)
            print("1. Lihat Daftar Garasi")
            print("2. Tambah Kendaraan Baru")
            print("3. Update Odometer")
            print("4. Cek Status Oli & Maintenance")
            print("5. Catat Ganti Oli/Maintenance")
            print("6. Hapus Kendaraan")
            print("0. Keluar")
            print("=" * 40)

            pilihan = input("Pilih Menu (0-6): ")

            if pilihan == "1":
                os.system("cls")
                garasi = my_garage.tunjukkan_kendaraan()
                vehicle_tabble(garasi)
                while True:
                    keluar = input_angka("Ketik '0' untuk keluar: ")
                    if keluar == 0:
                        break
                    else:
                        print("Input salah!")

            elif pilihan == "2":
                os.system("cls")
                while True:
                    jenis_kendaraan = input_choice(
                        "Masukkan jenis kendaraan (Motor/Mobil): ",
                        choices=["Motor", "Mobil"],
                    ).capitalize()
                    if jenis_kendaraan == "Motor":
                        nama = input_string("Masukkan Nama: ", min_len=3).capitalize()
                        cc = input_angka("Masukkan CC: ", min_len=2)
                        plat = input_string("Masukkan Plat Nomor:: ", min_len=3).upper()
                        kategori = input_choice(
                            "Masukkan Kategori (Matic/Manual/Kopling): ",
                            choices=["Matic", "Manual", "Kopling"],
                        ).capitalize()
                        motor = Motor(nama, cc, plat, kategori)
                        my_garage.tambah_kendaraan(motor)
                        print(
                            f"\nKendaraan {motor.nama} telah berhasil ditambahkan dengan ID {motor.id}."
                        )

                    elif jenis_kendaraan == "Mobil":
                        pass

            elif pilihan == "3":
                os.system("cls")
                while True:
                    garasi = my_garage.tunjukkan_kendaraan()
                    vehicle_tabble(garasi)
                    get_id = input_angka("Masukkan ID (0 Untuk Keluar): ")
                    if get_id == 0:
                        print("\nUpdate dibatalkan, kembali ke menu utama.")
                        break
                    for k in my_garage._daftar_kendaraan:
                        if get_id == k.id:
                            odo_baru = input_angka("Masukkan odometer baru: ")
                            k.update_odo(odo_baru)
                            print("\nOdometer telah diperbarui.")
                            print(f"Odometer: {k._odometer_lama} => {k._odometer}\n")
                            break
                    else:
                        print(f"Kendaraan dengan ID {get_id} tidak ditemukan.")

            elif pilihan == "4":
                os.system("cls")
                while True:
                    garasi = my_garage.tunjukkan_kendaraan()
                    vehicle_tabble(garasi)
                    get_id = input_angka("Masukkan ID (0 Untuk Keluar): ")
                    if get_id == 0:
                        print("\nUpdate dibatalkan, kembali ke menu utama.")
                        break
                    for k in my_garage._daftar_kendaraan:
                        if get_id == k.id:
                            k.status_oli()
                            if not k.status_oli():
                                print(
                                    f"Penting! Jangan lupa ganti oli jir udah terlewat {k._odometer - k._oli_terakhir}km ini"
                                )
                            else:
                                print(f"Aman aja, masih sisa {k.jarak_oli}km lagi kok!")
                            k.status_maintenance()
                            if not k.status_maintenance():
                                print(
                                    "Penting! Segera ke bengkel untuk maintenance berkala kendaraan."
                                )
                            else:
                                print(
                                    f"Aman aja, masih sisa {k.jarak_maintenance}km lagi kok!"
                                )
                            break
                    else:
                        print(f"Kendaraan dengan ID {get_id} tidak ditemukan.")

            elif pilihan == "5":
                pass

            elif pilihan == "6":
                pass

            elif pilihan == "0":
                print("\nProgram ditutup.")
                break

            else:
                print("\nPilihan tidak valid.")

        except Exception as e:
            print(f"\nError! Pesan: {e}")


if __name__ == "__main__":
    main()
