import pygame

class exitGame:
    def check(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()