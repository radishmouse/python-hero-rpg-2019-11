import time

class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print("%s faces the %s" % (hero.name, enemy.name))
        print("=====================")
        while hero.is_alive() and enemy.is_alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. use item")
            print("4. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                # print the use_item menu
                # user chooses an item
                # if they choose a Swap item
                # it gets applied
                # Here is the spot where item.apply()
                # would get called
                # hero's can_swap is now set to True
                item_choice = -1
                while item_choice < 0 or item_choice >= len(hero.items):
                    hero.view_inventory()
                    item_choice = int(input("Which item?"))
                hero.use_item(item_choice)
            elif user_input == 4:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
        if hero.is_alive():
            print("You defeated the %s" % enemy.name)
            return True
        else:
            print("YOU LOSE!")
            return False
