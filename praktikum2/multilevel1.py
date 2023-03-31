class Dosen:
    def __init__(self, nama, umur, nip):
        self.nama = nama
        self.umur = umur
        self.nip = nip
        
    def informasi(self):
        print(f"Nama: {self.nama}\nUmur: {self.umur}\nNIP: {self.nip}")

class Programmer(Dosen):
    def __init__(self, nama, umur, nip, skill):
        super().__init__(nama, umur, nip)
        self.skill = skill
    
    def keahlian(self):
        print(f"Skill: {self.skill}")

class Salary(Programmer):
    def __init__(self, nama, umur, nip,skill,gaji):
        super().__init__(nama,umur,nip,skill)
        self.gaji = gaji
        
    def penghasilan(self):
        print(f"Gaji: {self.gaji}")

salaryA = Salary("Lubis","40 Tahun", "123456", "Web Developer","RP 5000000")
salaryA.informasi()
salaryA.keahlian()
salaryA.penghasilan()
