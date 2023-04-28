try:
    nama = input ("Nama Lengkap: ")
    address = input("Alamat: ")
    if not address:
        raise EOFError("tidak ada input yang diterima") 
    
    print("Nama Lengkap: "+ nama)
    print("Alamat: " + address)
   
except EOFError as error:
    print(error)
    
    