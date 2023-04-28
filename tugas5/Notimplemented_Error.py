class Handphone:
    def sound(self):
        raise NotImplementedError("Method 'sound' belum diimplementasikan")

class Samsung(Handphone):
    def sound(self):
        return "Samsung"

class Redmi(Handphone):
    pass

def make_sound(handphone):
    try:
        return handphone.sound()
    except NotImplementedError as error:
        print(error)

samsung = Samsung()
redmi = Redmi()

print(make_sound(samsung))
print(make_sound(redmi))
