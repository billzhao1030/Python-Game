class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("Out of bullet!")

            return

        self.bullet_count -= 1
        print("fire!!")

class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None: # is => use to compare address
            print("No gun!!")

            return

        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("ak47")
ak47.add_bullet(50);

bill = Soldier("bill")
bill.gun = ak47
bill.fire()

