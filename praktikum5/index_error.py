my_list = ["1", "2", "3", "4", "5", "6"]

try:
    print(my_list[8])
except IndexError:
    print("Index tidak dapat ditemukan! Pastikan index sudah benar dan ada terdapat di dalam list!")