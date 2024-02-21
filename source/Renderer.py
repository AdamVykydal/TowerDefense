class Renderer:
    def render(self, screen, texture, x, y):
        screen.blit(texture, (x, y))