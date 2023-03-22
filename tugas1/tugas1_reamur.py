class Reamur:
    @staticmethod
    def to_celcius(reamur):
        return (reamur *5/4)
    
    @staticmethod
    def to_kelvin(reamur):
        return (reamur *5/4) +273
    
    @staticmethod
    def to_fahrenheit(reamur):
        return (reamur *9/4) +32
    
myreamurit = 100
print(f"Reamur Ke Celcius: {Reamur.to_celcius(myreamurit)}\nReamur Ke Kelvin:{Reamur.to_kelvin(myreamurit)}\nReamur Ke Fahrenheit: {Reamur.to_fahrenheit(myreamurit)}")

