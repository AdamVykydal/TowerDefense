from Bullet import Bullet

class PlayerTower:
    def __init__(self, texture, x, y):
        self.texture = texture
        self.y = y
        self.x = x
        self.speedUp = 0
        self.speedDown = 0
        self.Bullets = []
    def move(self):
        self.y -= self.speedUp
        self.y += self.speedDown
    def fire(self):
        self.Bullets.append(Bullet(30, 10, 1, self.x, self.y))
