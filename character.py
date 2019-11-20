import time

class Character(object):
    def __init__(self, name='<undefined>', health=10, power=5, coins=20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def is_alive(self):
        return self.health > 0
        # if self.health > 0:
        #     return True
        # else:
        #     return False

    def attack(self, enemy):        
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
