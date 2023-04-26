class MyClass:
    def __init__(self, a):
        self.a = a
    
    def my_method(self):
        print("Selamat Datang!")

my_object = MyClass(10)

try:
    my_object.my_attr
except AttributeError:
    print("Attribute tidak ditemukan! Mohon pastikan attribute sudah benar dan ada di dalam class.")