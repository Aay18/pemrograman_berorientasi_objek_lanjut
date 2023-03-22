#Nama   : Ayu Nurul Khairunnisa #
#NIM    : 221511020 #
#Kelas  : TI21K (K2 Konversi) #

class Celcius:
    def __init__(self,suhu, derajat):
        self.suhu = suhu
        self.derajat = derajat
    
    def info(self):
        print(f"Suhu saya {self.suhu} Derajat{self.derajat}")
        
celciusA= Celcius("30"," Celcius")
celciusA.info() 

