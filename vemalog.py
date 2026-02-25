# Vehicle Maintenance Log Project

import os
import utility as u
from models import Kendaraan, Motor, Garasi


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
                u.vehicle_table(garasi)
                while True:
                    keluar = u.input_angka("Ketik '0' untuk keluar: ")
                    if keluar == 0:
                        break
                    else:
                        print("Input salah!")

            elif pilihan == "2":
                os.system("cls")
                while True:
                    jenis_kendaraan = u.input_choice(
                        "Masukkan jenis kendaraan (Motor/Mobil): ",
                        choices=["Motor", "Mobil"],
                    ).capitalize()
                    if jenis_kendaraan == "Motor":
                        nama = u.input_string("Masukkan Nama: ", min_len=3).capitalize()
                        cc = u.input_angka("Masukkan CC: ", min_len=2)
                        plat = u.input_string(
                            "Masukkan Plat Nomor:: ", min_len=3
                        ).upper()
                        kategori = u.input_choice(
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
                    u.vehicle_table(garasi)
                    get_id = u.input_angka("Masukkan ID (0 Untuk Keluar): ")
                    if get_id == 0:
                        print("\nUpdate dibatalkan, kembali ke menu utama.")
                        break
                    for k in my_garage._daftar_kendaraan:
                        if get_id == k.id:
                            odo_baru = u.input_angka("Masukkan odometer baru: ")
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
                    u.vehicle_table(garasi)
                    get_id = u.input_angka("Masukkan ID (0 Untuk Keluar): ")
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
