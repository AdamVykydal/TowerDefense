class ManageEnemyes:
    def __init__(self, screen, renderer, enemyTexture, gameOver):
        self.screen = screen
        self.renderer = renderer 
        self.enemyTexure = enemyTexture
        self.gameOver = gameOver
    def manage(self, enemyes):
        for enemy in enemyes:
            enemy.move()
            self.gameOver.check(enemy)
            self.renderer.render(self.screen, self.enemyTexure, enemy.x, enemy.y)
