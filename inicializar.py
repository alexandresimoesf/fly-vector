import pygame
import pygame.font

class Texto():
    def __init__(self, texto, posicao):
        self.myfont = pygame.font.SysFont("Arial", 30)
        self.label = self.myfont.render(texto, 1, (255,255,255))

    def Show(self, screen, pos):
        screen.blit(pygame.image.load('unifei.png'), (5,5))
        screen.blit(pygame.image.load('lots.png'), ((700//2)-200,500))
        screen.blit(self.label, pos)
    
