class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('created unit {0}'.format(self.name))
        print('energy {0}, ability {1}'.format(self.hp, self.damage))

# marine1 = Unit('marine', 40, 5)
# marine2 = Unit('marine', 40, 5)
# tank = Unit('tank', 150, 35)
# wraith1 = Unit('wrath', 80, 5)
# print('name : {0}, ability: {1}'.format(wraith1.name, wraith1.damage))

# wraith2 = Unit('stealing wraith', 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print('{0} is now clocking'.format(wraith2.name))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print('{0} : attacking {1} time direction. [ability {2}]'\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
          print('{0} : damaged {1}'.format(self.name, damage))
          self.hp -= damage
          print('{0} : right now, you hp is {1}'.format(self.name, self.hp))
          if self.hp <= 0:
              print('{0} is destroyed.'.format(self.name))

firebat1 = AttackUnit('firebat', 50, 16)
firebat1.attack('5clock')

firebat1.damaged(25)
firebat1.damaged(25)