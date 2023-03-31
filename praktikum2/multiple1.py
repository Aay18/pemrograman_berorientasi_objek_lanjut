class Makeup:
    def __init__(self, nama_cushion):
        self.nama_cushion = nama_cushion
    
    def digunakan(self):
        print(f"{self.nama_cushion} sedang digunakan")
        
class Cushion:
    def __init__(self, ukuran, shade):
        self.ukuran = ukuran 
        self.shade = shade  
    
    def mengaplikasikan(self):
        print(f"Mengamplikasikan Cushion {self.shade} ")

class MakeupCushion(Makeup, Cushion):
    def __init__(self, nama_cushion, shade, ukuran):
        Makeup.__init__(self,nama_cushion)
        Cushion.__init__(self,ukuran,shade)
    
    def memakai(self):
        print(f"Memakai Cushion {self.nama_cushion}, Shade {self.shade}, Ukuran {self.ukuran}")

makeup_cushion = MakeupCushion("Pixy","Shade 02","Kecil")
makeup_cushion.digunakan()
makeup_cushion.mengaplikasikan()
makeup_cushion.memakai()
        
        
       