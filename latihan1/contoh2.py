class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def info(self):
        print(f"Nama saya {self.nama} dengan NIM {self.nim}")

mahasiswaA = Mahasiswa("Ayu Nurul Khairunnisa","221511020")
mahasiswaA.info()