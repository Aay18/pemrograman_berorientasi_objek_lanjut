class Fahrenheit:
    
    @staticmethod
    def to_celcius(fahrenheit):
        return (fahrenheit -32)*5/9
    
    @staticmethod
    def to_reamur(fahrenheit):
        return (fahrenheit -32)*4/9
    
    @staticmethod
    def to_kelvin(fahrenheit):
        return (fahrenheit -32)*5/9+273

myfahrenheit = 80
print(f"Fahrenheit Ke Celcius: {Fahrenheit.to_celcius(myfahrenheit)}\nFahrenheit Ke Reamur: {Fahrenheit.to_reamur(myfahrenheit)}\nFahrenheit Ke Kelvin:{Fahrenheit.to_kelvin(myfahrenheit)}")
    
    