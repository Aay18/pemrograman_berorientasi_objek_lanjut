import sys

try:
    a = sys.maxsize + 1
    b = a * b
except OverflowError as error:
    print(error)