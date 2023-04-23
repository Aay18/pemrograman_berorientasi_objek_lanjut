# Mengatasi IndexError
list_angka = [1, 2, 3]
try:
    value = list_angka[20]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")
