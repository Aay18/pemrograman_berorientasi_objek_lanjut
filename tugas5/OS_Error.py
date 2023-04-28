try:
    file = open("filebts.txt", "r")
except OSError as error:
    print(error)