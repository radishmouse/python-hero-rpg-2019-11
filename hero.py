import time
from character import Character
import random

# Dealing with Armor
# - [X] give Hero an "armor" attribute/property
# - [X] when receiving damage, reduce by the amount of hero's armor
# - [X] create an Armor class
# - [X] add Armor to the Store
from swap import Swap
class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        self.armor = 0
        self.items = [Swap()]
        self.can_swap = False
        self.swapped_with_whom = None

    def attack(self, enemy):
        if not self.is_alive():
            return
        self.swap_power(enemy)

        print("%s attacks %s" % (self.name, enemy.name))

        # setup
        damage = self.power

        # work
        if random.random() <= 0.2: # 20% chance of double damage
            damage = self.power * 2
        
        # result
        enemy.receive_damage(damage)

        time.sleep(1.5)

    def receive_damage(self, points):
        damage = points - self.armor
        if damage < 0:
            damage = 0
        super().receive_damage(damage)
        self.reset_swap()

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        # item.apply(self)
        self.items.append(item)
    
    def view_inventory(self):
        i = 0
        for item in self.items:
            print(f"{i}: {item.name}")
            i += 1

    def use_item(self, index):
        item = self.items.pop(index)
        item.apply(self)
    
    def swap_power(self, enemy):
        if self.can_swap:
            print("It's swap time!")
            self.swapped_with_whom = enemy
            self.power, enemy.power = enemy.power, self.power            
    
    def reset_swap(self):
        if self.swapped_with_whom:
            self.can_swap = False
            self.power, self.swapped_with_whom.power = self.swapped_with_whom.power, self.power            
            print("Powers have been swapped back...")
            
            self.swapped_with_whom = None
