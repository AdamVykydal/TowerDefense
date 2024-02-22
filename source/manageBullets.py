from BulletCollistions import BulletCollisions

class ManageBullets:
    def __init__(self, screen, renderer, bulletTexture) -> None:
        self.renderer = renderer
        self.bulletCollistions = BulletCollisions()
        self.screen = screen
        self.bulletTexture = bulletTexture
    
    def manage(self, bullets, enemySpawner):
        for bullet in bullets:
            bullet.move()
            
            hit, hitedEnemy = self.bulletCollistions.check(bullet, enemySpawner.enemyes, bullet.hitedEnemyes)
            if hit:
                if bullet.penetrate(hitedEnemy):
                    bullets.remove(bullet)
                
            if bullet.x <= 0:
                bullets.remove(bullet)
                enemySpawner.spawn()
            
            self.renderer.render(self.screen, self.bulletTexture, bullet.x, bullet.y)
    

