from random import randint
class Axe():
    def __init__(self,  health = 700, mana = 291, armor = 2.33, damage = 54, movespeed = 310):
        self.healt = health
        self.mana = mana
        self.armor = armor
        self.damage = damage
        self.movespeed = movespeed

    def BerserkersCall(self, mana = 80, armor = 30):
        if self.mana < mana:
            print("I HAVE NO MANA!!1!!1")
        else:
            print("CAM TO AXE")
            self.mana -= mana
            self.armor += armor

    def BattyrHunger(self, mana = 50, movespeed = 0.1):
        if self.mana < mana:
            print("AXE HAS NO MANA")
        else:
            print("PROVE YOURSELF")
            self.mana -= mana
            self.movespeed += movespeed * self.movespeed

    def CounterHelix(self, chance = randint(0,2)):
        return ("ВЖЖх" if chance == 1 else "KRUTIIS BLYAT")

    def CullingBlade(self, mana = 60, chance = randint(0,1), movespeed = 0.3):
        if chance and self.mana > mana:
            self.movespeed *= movespeed
            self.mana -= mana
            print("HOHO YEAH")
            self.CullingBlade()
        elif self.mana < mana:
            print("NO mana ")


    def info(self):
        print(f"{self.healt} = hp {self.mana} = mp {self.armor} = armor {self.movespeed} = ms {self.damage} = dmg")



axe = Axe()
axe.info()
axe.BerserkersCall()
axe.BattyrHunger()
axe.info()
print(axe.CounterHelix())
axe.info()
axe.CullingBlade()
