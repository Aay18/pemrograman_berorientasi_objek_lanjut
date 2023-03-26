class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def belajar(self):
        print(self.nama, "Sedang Belajar")
        
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan 
        
    def bekerja(self):
        print(self.nama, "Sedang Bekerja")
        
class MahasiswaPekerja:
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    
    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")

mhs_pekerja = MahasiswaPekerja("Ayu Nurul Khairunnisa","190001","Programmer")
mhs_pekerja.belajar()
mhs_pekerja.bekerja()
mhs_pekerja.bersosialisasi()