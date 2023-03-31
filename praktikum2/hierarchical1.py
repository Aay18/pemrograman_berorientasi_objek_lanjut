class Makeup:
    def __init__(self, nama):
        self.nama = nama    
    def get_nama(self):
        return self.nama

class Cushion(Makeup):
    def __init__(self, nama):
        super().__init__(nama)
    def get_nama(self):
        return self.nama

class Lipstick(Makeup):
    def __init__(self, nama, shade):
        super().__init__(nama)
        self.shade = shade
    def get_shade(self):
        return self.shade

#Hierarchical Inheritance
class LipstickWardah(Lipstick):
    def __init__(self, nama, shade, harga):
        super().__init__(nama, shade)
        self.harga = harga
    def get_harga(self):
        return self.harga
    
lipstickA = LipstickWardah("Wardah","12","RP 30000")
print(f"Lipstick {Makeup.get_nama(lipstickA)} dengan shade {Lipstick.get_shade(lipstickA)} dan harganya {LipstickWardah.get_harga(lipstickA)}")

