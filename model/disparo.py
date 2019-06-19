import pygame

class Missil(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagemMissil = pygame.image.load('imagens/Municao(naveprincipal).JPG')
        self.rect = self.imagemMissil.get_rect()
        self.velocidadeDisparo = 3
        self.rect.top = posY
        self.rect.left = posX
    def percurso(self):
        self.rect.top = self.rect.top-self.velocidadeDisparo
    def desenhar(self, superficie):
        superficie.blit(self.imagemMissil, self.rect)