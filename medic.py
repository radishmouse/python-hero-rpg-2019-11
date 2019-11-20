import random
from chracter import Character
class Medic(Character):
    
    def receive_damage(self, points):
        super().receive_damage(points)

        if self.is_alive():
            # 20% chance of recuperating
            if random.random() <= 0.2:
                self.health += 2
                print(f"{self.name} recuperates 2 points!")

            
