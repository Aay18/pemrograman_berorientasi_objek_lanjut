class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("The Animal Speaks")
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print("The Dog Barks")

class Bulldog(Dog):
    def __init__(self, name, breed, origin):
        super().__init__(name,breed)
        self.origin = origin
    
    def speak(self):
        print("The Bulldog Growls")

bulldogA = Bulldog("American Bulldog","Dogs","Origin")
bulldogA.speak()
