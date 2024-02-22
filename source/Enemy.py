class Enemy:
    def __init__(self, speed, hp, x, y, ):
        self.x = x
        self.y = y
        self.speed = speed
        self.hp = hp 
    def move(self):
        self.x += self.speed 
    def getDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True