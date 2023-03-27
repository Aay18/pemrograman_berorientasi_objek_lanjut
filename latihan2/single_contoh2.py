class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def berbicara(self):
        print(f"{self.nama} sedang berbicara")

class Dosen(Manusia):
    def __init__(self,nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar")
        
dosenA = Dosen("Pak Freddy",35, "123456")
dosenA.berbicara() #output: Budi sedang berbicara
dosenA.mengajar() #output: Budi dengan NIP 123456 sedang mengajar.