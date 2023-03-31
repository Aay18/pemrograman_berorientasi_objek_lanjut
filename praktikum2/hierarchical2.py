class SmartPhone:
    def __init__(self, nama):
        self.nama = nama
    def get_nama(self):
        return self.nama

class Android(SmartPhone):
    def __init__(self, nama, merk):
        super().__init__(nama)
        self.merk = merk
    def get_merk(self):
        return self.merk

class IOS(SmartPhone):
    def __init__(self, nama, merk, kapasitas):
        super().__init__(nama,merk)
        self.kapasitas = kapasitas
    def get_kapasitas(self):
        return self.kapasitas
    
#Hierarchical Inheritance
class Samsung(Android):
    def __init__(self, nama, merk, warna):
        super().__init__(nama, merk)
        self.warna = warna
    def get_warna(self):
        return self.warna

samsungA = Samsung("Samsung", "Galaxy J1", "Hitam")
print(f"{SmartPhone.get_nama(samsungA)} {Android.get_merk(samsungA)} Warna {Samsung.get_warna(samsungA)}")

