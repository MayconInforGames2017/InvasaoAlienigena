import pygame
from model import disparo
#from menu_inicial import menu_selecao
#herdar do sprite
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagemNave = pygame.image.load('imagens/NavePrincipal.png')
        self.imagemExplosao = pygame.image.load('imagens/Explosao.PNG')
        self.rect = self.imagemNave.get_rect()
        #posição
        self.rect.centerx = 250
        self.rect.centery = 383
        self.velocidade = 2
        self.vida = True
        self.lista_Disparo = []
        self.somDisparo = pygame.mixer.Sound('sons/TiroNave.wav')
    def movimentoNave(self):
        if self.rect.left <= -30:
           self.rect.left = -30
        if self.rect.right > 530:
           self.rect.right = 530
        if self.rect.top <= -15:
           self.rect.top = -15
        if self.rect.bottom > 415:
           self.rect.bottom = 415
    def disparar(self,x, y):
        missil = disparo.Missil(x,y)
        self.somDisparo.play()
        self.lista_Disparo.append(missil)
    def desenhar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagemNave, self.rect)
        else:
            superficie.blit(self.imagemExplosao, self.rect)
    #def carregar(self, menu):
        #self.menu = menu_selecao = 1
