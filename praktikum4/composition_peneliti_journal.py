class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
    
    def tulis_jurnal(self, judul, isi):
        jurnal = Jurnal(judul, isi, self)
        return jurnal
    
class Jurnal:
    def __init__(self, judul, isi, penulis):
        self.judul = judul
        self.isi = isi
        self.penulis = penulis

p1 = Peneliti("Ayu Nurul Khairunnisa", "Ilmu Kesehatan")

j1 = p1.tulis_jurnal("Analisis Bahasa Indonesia Sebagai Bahasa Nasional","Bahasa Indonesia lahir sebagai bahasa nasional sejak pemuda mengucapkan sumpah. Dampak dari peristiwa ini cukup besar untuk membangkitkan semangat juang rakyat untuk kemerdekaan.")

print(j1.judul)
print(j1.penulis.nama)

