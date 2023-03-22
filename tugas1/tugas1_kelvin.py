class Kelvin:
    @staticmethod
    def to_celcius(kelvin):
        return(kelvin -273)
    
    @staticmethod
    def to_reamur(kelvin):
        return(kelvin -273)*4/5
    
    @staticmethod
    def to_fahrenheit(kelvin):
        return(kelvin -273)*9/5+32

mykelvin = 100
print(f"Kelvin ke Celcius: {Kelvin.to_celcius(mykelvin)}\nKelvin Ke Reamur: {Kelvin.to_reamur(mykelvin)}\nKelvin Ke Fahrenheit: {Kelvin.to_fahrenheit(mykelvin)}")

