my_dict = {"Nama": "Ayu Nurul Khairunnisa", "Umur": "22"}

try:
    print(my_dict["Alamat"])
except KeyError:
    print("Key tidak dapat ditemukan! Pastikan key sudah benar dan sudah di dalam dictionary!")