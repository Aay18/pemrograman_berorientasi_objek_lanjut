class Kalkulator:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod 
    def subtract(x,y):
        return x - y
    @staticmethod
    def multiply(x,y):
        return x*y
    
    @staticmethod 
    def divide(x,y):
        if y == 0:
            raise ValueError('Tidak dapat dibagi dengan nol')
        return x/y
        
#Memanggil metode statis add() dan substract() di dalam class Math
print(Kalkulator.add(3,5))
print(Kalkulator.subtract(10,7))

#Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(4,6))
print(Kalkulator.divide(12,4))