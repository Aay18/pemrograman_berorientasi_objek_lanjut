number = 5
string = "abcde"

try:
    result = number + string
    print(result)
except TypeError:
    print("Terjadi kesalahan pada tipe data! Pastikan tipe data variabel sudah benar!")
