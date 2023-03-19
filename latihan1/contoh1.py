class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    
    def info(self):
        print(f"Mobil: {self.merk}\nWarna:{self.warna}")
        
mobilA = Mobil("Mobil Toyota", "Warna Hitam")
mobilA.info()