#Mengatasi Error Menggunakan ZeroDivisionError


try:
    x = 3
    y = x / 0
except ZeroDivisionError:
    print("Terjadi kesalahan pembagian dengan nol!")