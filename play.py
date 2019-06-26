import pygame, sys
from pygame.locals import *
#importação dos modelos

from model import jogador
from model import asteroide
from random import randint
from time import process_time

#variaveis
altura =  500
largura = 400

lista_Asteroide = []
colorFonte = (0, 0, 0)
posX = 0
posY = 0
pontos = 0
#boolean Jogador
global jogando
jogando = True

#função para carregar NaveInimiga
def carregarAsteroides(x,y):
    meteoro = asteroide.Asteroide(x,y)
    lista_Asteroide.append(meteoro)

def gameOver():
    global jogando
    jogando = False
    for meteoro in lista_Asteroide:
        lista_Asteroide.remove(meteoro)
#função principal
def Jogo(screen):

    pygame.init()
    janela = pygame.display.set_mode((altura, largura))
    # som de colisões
    somColisao = pygame.mixer.Sound('sons/ExplosaoNaveInimiga.wav')
    #imagem de fundo
    fundo = pygame.image.load('imagens/Mapa.JPG')
    #janela.blit(fundo, (0,0))
    #titulo
    pygame.display.set_caption('Invasão Alienigina')
    #criando objeto jogador
    nave = jogador.Nave()
    contador = 0
    pontos = 0
    #pontos marcados
    Marcador = pygame.font.SysFont("Arial", 20)

    #som de fundo
    pygame.mixer.music.load('sons/MusicaFundo.ogg')
    pygame.mixer.music.set_volume(0.5)
    #números de repertições
    pygame.mixer.music.play(50)

    while True:
        janela.blit(fundo, (0,0))
        nave.desenhar(janela)
        keys = pygame.key.get_pressed()
        #pontuação
        TextoMarcador = Marcador.render("Pontos: " +str(pontos), 0, colorFonte)
        janela.blit(TextoMarcador, (0,0))
        #tempo e coordenadas do asteroide
        tempo = process_time()
        #asteroide a cada segundo
        if tempo - contador > 1:
            contador = tempo
            posX = randint(2,278)
            carregarAsteroides(posX, posY)
        #lista de asteroides
        if len(lista_Asteroide) > 0:
            for x in lista_Asteroide:
                x.desenhar(janela)
                x.percorrido()
                if x.rect.top > 500:
                    lista_Asteroide.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        lista_Asteroide.remove(x)
                        somColisao.play()
                        nave.vida = False
                        #somColisao.stop()
                        gameOver()

        if len(nave.lista_Disparo) > 0:
            for x in nave.lista_Disparo:
                x.desenhar(janela)
                x.percurso()
                if x.rect.top <- 10:
                    nave.lista_Disparo.remove(x)
                else:
                    for meteoro in lista_Asteroide:
                        if x.rect.colliderect(meteoro.rect):
                            somColisao.play()
                            pontos += 1
                            lista_Asteroide.remove(meteoro)
                            nave.lista_Disparo.remove(x)

        nave.movimentoNave()
        for evento in pygame.event.get():

                #fechar o jogo com X
            if evento.type==QUIT:
                 pygame.quit()
                 sys.exit()
            if evento.type==pygame.KEYDOWN:
                 if evento.key==K_SPACE:
                     x,y = nave.rect.center
                     nave.disparar(x-1,y-22)

        if keys [K_LEFT]:
            nave.rect.left -= nave.velocidade
        if keys [K_RIGHT]:
            nave.rect.right += nave.velocidade
        if keys [K_UP]:
            nave.rect.top -= nave.velocidade
        if keys [K_DOWN]:
            nave.rect.bottom += nave.velocidade

        if jogando == False:
            FonteGameOver = pygame.font.SysFont("Arial", 30)
            TextoGameOver = FonteGameOver.render("Game Over!", 0, colorFonte)
            janela.blit(TextoGameOver, (140, 350))
            pygame.mixer.music.fadeout(3000)

        pygame.display.update()

