try:
    with open('file.txt', 'w', encoding='ascii') as f:
        f.write('Hallo, Dunia!')  
except UnicodeEncodeError:
    print("Error: Failed to encode the string with ASCII encoding")