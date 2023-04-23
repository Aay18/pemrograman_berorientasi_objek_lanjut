#Mengatasi Error

try:
    my_list = [1,2,3]
    my_list.remove(4)
except ValueError:
    print("Eror: Elemen tidak ada di dalam list!")

