class Penulis:
    def __init__(self, nama):
        self.nama = nama
    
    def tulis_buku(self, judul, halaman):
        buku = Buku(judul, halaman, self)
        return buku
    
class Buku:
    def __init__(self, judul, halaman, penulis):
        self.judul = judul
        self.halaman = halaman
        self.penulis = penulis

p1 = Penulis("Agnes Davonar")
b1 = p1.tulis_buku("Surat Kecil Untuk Tuhan", "201 Halaman")


print(b1.judul)
print(b1.penulis.nama)