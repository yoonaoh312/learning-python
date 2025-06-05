class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('created unit {0}'.format(self.name))
        print('energy {0}, ability {1}'.format(self.hp, self.damage))

marine1 = Unit('marine', 40, 5)
marine2 = Unit('marine', 40, 5)
tank = Unit('tank', 150, 35)
wraith1 = Unit('wrath', 80, 5)
print('name : {0}, ability: {1}'.format(wraith1.name, wraith1.damage))

wraith2 = Unit('stealing wraith', 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print('{0} is now clocking'.format(wraith2.name))