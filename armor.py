class Armor:
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor = 2
        print(f"{hero.name}'s armor increased to {hero.armor}")