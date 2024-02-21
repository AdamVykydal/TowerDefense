import pygame

class HandleInput:
    def __init__(self, playerTower):
        self.playerTower = playerTower
        self.speed = 10
    
    def check(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL:
                    self.playerTower.fire()
                if event.key == pygame.K_UP:
                    self.playerTower.speedUp = self.speed
                if event.key == pygame.K_DOWN:
                    self.playerTower.speedDown = self.speed
           
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.playerTower.speedUp = 0
                if event.key == pygame.K_DOWN:
                    self.playerTower.speedDown = 0