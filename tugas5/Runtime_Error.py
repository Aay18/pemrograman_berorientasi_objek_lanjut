def divide(a, y):
    if y == 0:
        raise RuntimeError("pembagian dengan 0")
    else:
        return a / y

try:
    result = divide(10, 0)
except RuntimeError as error:
    print(error)