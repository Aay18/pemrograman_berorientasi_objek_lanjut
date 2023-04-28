def divide(num1, num2):
    assert num2 != 0, "Tidak dapat di bagi dengan nol"
    return num1 / num2

try:
    result = divide(100, 0)
    print(result)
except AssertionError as error:
    print(error)
    
    