import random
from Enemy import Enemy

class EnemySpawner:
    def __init__(self):
        self.enemyes = []
    def spawn(self):
        speed = random.randint(1, 10)
        startY = random.randint(50, 1030)
        
        self.enemyes.append(Enemy(1, 50, 0, startY))