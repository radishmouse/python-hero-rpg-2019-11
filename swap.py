class Swap:
    name = 'swap'
    cost = 100
    def apply(self, hero):
        hero.can_swap = True
        print("%s's can swap powers with enemy for one turn." % (hero.name, ))
