try:
    big_list = [10] * (10**9)
except MemoryError:
    print("Terjadi error, list terlalu besar untuk di handle!")
