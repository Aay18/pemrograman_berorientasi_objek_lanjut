#Nama   : Ayu Nurul Khairunnisa #
#NIM    : 221511020 #
#Kelas  : TI21K (K2 Konversi) #

class Celcius:
    @staticmethod
    def to_reamur(celcius):
        return(celcius *4/5)
    
    @staticmethod
    def to_fahrenheit(celcius):
        return(celcius *9/5)+32
    
    @staticmethod
    def to_kelvin(celcius):
        return(celcius)+273
    
mycelcius = 100
mycelciusit = Celcius.to_kelvin(mycelcius)
print(mycelciusit)

