class Bullet:
    def __init__(self, speed, x, y):
        self.x = x
        self.y = y
        self.speed = speed
    def move(self):
        self.x -= self.speed
    