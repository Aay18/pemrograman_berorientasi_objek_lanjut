#Single Inheritance
class Team:
    def __init__(self, nama_team):
        self.nama_team = nama_team
    
    def bermain(self):
       print(f"Team {self.nama_team} sedang bermain")

#Single Inheritance
class TipeHero:
    def __init__(self, tipe_hero):
        self.tipe_hero = tipe_hero
    
    def menggunakan(self):
        print(f"Menggunakan {self.tipe_hero}")

#Multiple_Inheritance
class Player(Team, TipeHero):
    def __init__(self, nama_team, tipe_hero, jenis_permainan):
        Team.__init__(self,nama_team)
        TipeHero.__init__(self,tipe_hero)
        self.jenis_permainan = jenis_permainan
    
    def dipilih(self):
        print(f"sedang dipilih untuk bermain di {self.jenis_permainan}")

teamA = Player("Barracuda","Fighter","Rank")
teamA.bermain()
teamA.menggunakan()
teamA.dipilih()


    
    
