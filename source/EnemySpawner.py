import random
from Enemy import Enemy

class EnemySpawner:
    def __init__(self):
        self.enemyes = [Enemy(5, 100, 100), Enemy(5, 500, 400)]
    def spawn(self):
        speed = random.randint(1, 10)
        startY = random.randint(50, 1030)
        
        self.enemyes.append(Enemy(speed, 0, startY))