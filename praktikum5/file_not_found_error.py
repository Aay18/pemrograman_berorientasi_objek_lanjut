try:
    file = open("not_file.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File tidak dapat ditemukan! Pastikan file sudah tersedia di direktori yang benar!")