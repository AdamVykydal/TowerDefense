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
            if self.bulletCollistions.check(bullet, enemySpawner.enemyes):
                bullets.remove(bullet)
                enemySpawner.spawn()

            print(bullets)
            
            self.renderer.render(self.screen, self.bulletTexture, bullet.x, bullet.y)

