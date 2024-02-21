class BulletCollisions:
    def check(self, bullet, enemyes):
        for enemy in enemyes: 
            if abs(bullet.y - enemy.y) <= 30 and abs(bullet.x - enemy.x) <= 50: 
                enemyes.remove(enemy)
                return True
        return False
                