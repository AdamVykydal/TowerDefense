import pygame
from exitGame import exitGame
from PlayerTower import PlayerTower
from Renderer import Renderer
from HandleInput import HandleInput
from Enemy import Enemy
from manageBullets import ManageBullets

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screenW, self.screenH = pygame.display.get_surface().get_size()
        self.clock = pygame.time.Clock()
        self.exitGame = exitGame()
        self.playerTowerTexture = pygame.image.load("recources\img\playerTower.png").convert_alpha()
        self.bulletTexture = pygame.image.load("recources\img\\bullet.png").convert_alpha()
        self.playerTowerSpeed = 10
        self.playerTowerY = self.screenH / 2
        self.playerTowerX = 1800
        self.playerTower = PlayerTower(self.playerTowerTexture, self.playerTowerX, self.playerTowerY)
        self.renderer = Renderer()
        self.handleInput = HandleInput(self.playerTower)
        self.enemyes = [Enemy(5, 100, 100), Enemy(5, 500, 400)]
        self.manageBullets = ManageBullets(self.screen, self.renderer, self.bulletTexture) 

    
    def run(self):
        while True:
            self.clock.tick(60)
            events = pygame.event.get()
            self.exitGame.check(events)
            self.screen.fill((255, 0, 0))
            self.handleInput.check(events)
            self.playerTower.move()
            self.renderer.render(self.screen, self.playerTower.texture, self.playerTower.x, self.playerTower.y)
            self.manageBullets.manage(self.playerTower.Bullets, self.enemyes)
            for enemy in self.enemyes:
                enemy.move()
                self.renderer.render(self.screen, self.playerTower.texture, enemy.x, enemy.y)
            
            pygame.display.update()
