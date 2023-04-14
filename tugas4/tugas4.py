class Handphone:
    def __init__(self, nama):
        self.nama = nama
    
    def __str__(self):
        return f"{self.nama}"
    
class ProdukHandphone:
    def __init__(self, nama, daftar_handphone):
        self.nama = nama
        self.daftar_handphone = daftar_handphone
    
    def tambah_handphone(self, handphone):
        self.daftar_handphone.append(handphone)
        
    def __str__(self):
        return f"{self.nama} merupakan daftar handphone dari {', '.join(str(handphone) for handphone in self.daftar_handphone)}"
        
handphone1 = Handphone("Samsung")
handphone2 = Handphone("Oppo")

samsung_j1 = ProdukHandphone("Samsung J1", [handphone1])
oppo_neo = ProdukHandphone("Opponeo", [handphone2])

print(samsung_j1)
print(oppo_neo)