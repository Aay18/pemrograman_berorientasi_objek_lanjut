class Hero:
    def __init__(self,nama,damage):
        self.nama = nama
        self.damage = damage
    
    def bergerak(self):
        print(self.damage, "damage")

class Fighter(Hero):
    def __init__(self, nama, damage, item ):
        super().__init__(nama,damage)
        self.item = item
    
    def menyerang(self):
        print(self.nama, "menyakitkan")

fighterA = Fighter("Aldos", 4000, "Cursed Helmet")
fighterA.bergerak()
fighterA.menyerang()
        
    
    