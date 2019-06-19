import pygame

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagemAsteroide = pygame.image.load('imagens/NaveInimiga.png')
        self.rect = self.imagemAsteroide.get_rect()
        self.velocidade = 1
        self.rect.top = posY
        self.rect.left = posX
        self.lista_Asteroide = []
    def percorrido(self):
        self.rect.top = self.rect.top + self.velocidade
    def desenhar(self, superficie):
        superficie.blit(self.imagemAsteroide, self.rect)
