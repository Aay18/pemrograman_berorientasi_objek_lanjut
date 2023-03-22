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

mycelciusit = 100
print(f"Celcius Ke Reamur: {Celcius.to_reamur(mycelciusit)}\nCelcius Ke Fahrenheit: {Celcius.to_fahrenheit(mycelciusit)}\nCelcius Ke Kelvin: {Celcius.to_kelvin(mycelciusit)}")


