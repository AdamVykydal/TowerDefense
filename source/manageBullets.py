from BulletCollistions import BulletCollisions
class ManageBullets:
    def __init__(self, screen, renderer, bulletTexture) -> None:
        self.renderer = renderer
        self.bulletCollistions = BulletCollisions()
        self.screen = screen
        self.bulletTexture = bulletTexture
    def manage(self, bullets, enemyes):
        for bullet in bullets:
            bullet.move()
            if self.bulletCollistions.check(bullet, enemyes):
                bullets.remove(bullet)

            self.renderer.render(self.screen, self.bulletTexture, bullet.x, bullet.y)

