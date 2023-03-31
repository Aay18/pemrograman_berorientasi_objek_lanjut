class Kendaraan:
    def __init__(self, brand):
        self.brand = brand
    def get_brand(self):
        return self.brand 
    
class Sepeda(Kendaraan):
    def __init__(self, brand, merk):
        super().__init__(brand)
        self.merk = merk
    def get_merk(self):
        return self.merk

class Motor(Kendaraan):
    def __init__(self, brand, merk, tahun):
        super().__init__(brand, merk)
        self.tahun = tahun
    def get_tahun(self):
        return self.tahun

class SepedaListrik(Sepeda):
    def __init__(self, brand, merk, tahun,kapasitas_baterai):
        super().__init__(brand, merk)
        self.kapasitas_baterai = kapasitas_baterai
    def get_kapasitas_baterai(self):
        return self.kapasitas_baterai

sepedalistrikA = SepedaListrik("Goda","Sepeda Listrik Goda 140 New","Tahun 2023","12 Jam")
print(f"{Sepeda.get_merk(sepedalistrikA)} dengan kapasitas baterai {SepedaListrik.get_kapasitas_baterai(sepedalistrikA)}")

