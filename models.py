# Models


class Kendaraan:
    def __init__(self, nama, cc, plat, jenis):
        self.nama = nama
        self.cc = cc
        self.plat = plat
        self.jenis = jenis


class Motor(Kendaraan):
    def __init__(self, nama, cc, plat, kategori):
        super().__init__(nama, cc, plat, jenis="Motor")
        self.kategori = kategori
        self._odometer = 0
        self._oli_terakhir = 0
        self._oli_interval = 2000
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
                jarak_maintenance = interval_maintenance(
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
        self.gid = 1
        self._daftar_kendaraan = []
        self.capacity = 5

    def cari_kendaraan(self, id):
        for k in self._daftar_kendaraan:
            if k.id == id:
                return k
        return None

    def tunjukkan_kendaraan(self):
        if not self._daftar_kendaraan:
            raise ValueError("Garasi anda kosong.")
        return self._daftar_kendaraan

    def tambah_kendaraan(self, obj_kendaraan):
        if len(self._daftar_kendaraan) >= self.capacity:
            raise RuntimeError("Garasi anda penuh.")
        obj_kendaraan.id = self.gid
        self._daftar_kendaraan.append(obj_kendaraan)
        self.gid += 1

    def hapus_kendaraan(self, id):
        target = self.cari_kendaraan(id)
        if not target:
            raise KeyError(f"Kendaraan dengan ID {id} tidak ditemukan.")
        self._daftar_kendaraan.remove(target)
