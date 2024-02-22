class BulletCollisions:
    def check(self, bullet, enemyes, hitedEnemyes):
        for enemy in enemyes: 
            if abs(bullet.y - enemy.y) <= 30 and abs(bullet.x - enemy.x) <= 50: 
                for hitedEnemy in hitedEnemyes:
                    if enemy == hitedEnemy:
                        return False, None
                if enemy.getDamage(10):
                    enemyes.remove(enemy)
                    return True, None
                return True, enemy
        return False, None
                    