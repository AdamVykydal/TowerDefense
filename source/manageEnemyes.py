class ManageEnemyes:
    def __init__(self, screen, renderer, enemyTexture):
        self.screen = screen
        self.renderer = renderer 
        self.enemyTexure = enemyTexture
    def manage(self, enemyes):
        for enemy in enemyes:
            enemy.move()
            self.renderer.render(self.screen, self.enemyTexure, enemy.x, enemy.y)