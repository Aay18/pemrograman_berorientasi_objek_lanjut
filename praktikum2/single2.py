class Televisi:
    def __init__(self, merk):
        self.merk = merk
        
    def ditonton(self):
        print(f"{self.merk} sedang ditonton")
    
class Siaran(Televisi):
    def __init__(self, merk, nama_siaran, lokasi, nama_program_acara ):
        super().__init__(merk)
        self.nama_siaran = nama_siaran
        self.lokasi = lokasi
        self.nama_program_acara = nama_program_acara
    
    def menonton(self):
        print(f"Merk Televisi: {self.merk}\n Siaran: {self.nama_siaran}\n Lokasi: {self.lokasi}\n Program Acara: {self.nama_program_acara}")

siaranA = Siaran("Televisi Merk Samsung","Trans 7","Jakarta","Lapor Pak")
siaranA.ditonton()
siaranA.menonton()

