#Single Inheritance
class Kendaraan:
    def __init__(self, brand):
        self.brand = brand
    
    def digunakan(self):
        print(f"{self.brand} sedang digunakan")
    
#Single Inheritance
class Sepeda:
    def __init__(self, merk):
        self.merk = merk 
    
    def memilih(self):
        print(f"Memilih sepeda {self.merk} ")

class SepedaListrik(Kendaraan, Sepeda):
    def __init__(self, brand, merk, kapasitas_baterai):
        Kendaraan.__init__(self, brand)
        Sepeda.__init__(self,merk)
        self.kapasitas_baterai = kapasitas_baterai
    
    def memakai(self):
        print(f"Memakai Sepeda Listrik {self.merk} dengan kapasitas baterai {self.kapasitas_baterai}")

sepedaA = SepedaListrik("Goda","Sepeda Listrik Goda 140 New","12 Jam")
sepedaA.digunakan()
sepedaA.memilih()
sepedaA.memakai()
        
        
       