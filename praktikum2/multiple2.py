class Team:
    def __init__(self, nama_team):
        self.nama_team = nama_team
    
    def bermain(self):
       print(f"Team {self.nama_team} sedang bermain")

class TipeHero:
    def __init__(self, tipe_hero):
        self.tipe_hero = tipe_hero
    
    def menggunakan(self):
        print(f"Menggunakan {self.tipe_hero}")

class Hero(Team, TipeHero):
    def __init__(self, nama_team, tipe_hero,damage):
        Team.__init__(self, nama_team)
        TipeHero.__init__(self, tipe_hero)
        self.damage = damage
    
    def dipilih(self):
        print(f"Hero {self.tipe_hero} sedang dipilih dengan damage yang {self.damage}")

teamA = Hero("Barracuda","Fighter","Kuat")
teamA.bermain()
teamA.menggunakan()
teamA.dipilih()
    
    
