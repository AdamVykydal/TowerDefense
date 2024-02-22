class Bullet:
    def __init__(self, speed, damage, pierce, x, y):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.pierce = pierce
        self.hitedEnemyes = []
    def move(self):
        self.x -= self.speed
    def penetrate(self, hitedEnemy):
        self.pierce -= 1
        if self.pierce <= -1:
            return True
        else:
            self.hitedEnemyes.append(hitedEnemy)