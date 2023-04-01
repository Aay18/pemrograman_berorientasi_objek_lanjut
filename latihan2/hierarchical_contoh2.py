class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_salary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, age, salary, departement):
        super().__init__(name, age, salary)
        self.departement = departement
        
    def get_departement(self):
        return self.departement
    
class Programmer(Employee):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language
    
    def get_language(self):
        return self.language

#Hierarchical Inheritance
class SeniorProgrammer(Programmer):
    def __init__(self, name, age, salary, language, level):
        super().__init__(name, age, salary, language)
        self.level
        
    def get_levek(self):
        return self.level