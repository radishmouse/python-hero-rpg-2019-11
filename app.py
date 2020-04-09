from hero import Hero
from zombie import Zombie
from goblin import Goblin
from wizard import Wizard
from battle import Battle
from store import Store

hero = Hero('Oakley')
zombie = Zombie()
enemies = [Goblin('Bob'), Wizard('Jethro')]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
print("But not you Chris Aquino")
