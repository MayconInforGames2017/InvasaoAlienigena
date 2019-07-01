import pygame, sys
from pygame.locals import *
from pygame import KEYDOWN, KEYUP
from pygame import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_RETURN, K_ESCAPE, K_a, K_s, K_d, K_w
from play import Jogo

pygame.init()
a = 800 #altura da janela
l = 600 #largura da janela
fundoMenu = pygame.image.load('imagens/Menu.jpg')
fixo = True
selecao = True
screen = pygame.display.set_mode((a, l), 0, 32 )
screen_menu = pygame.Surface((a, l), 0, 32 )
musica = 'sons/musicaFundo.ogg'
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)


def fixo():
    fonte = pygame.font.SysFont("Agency FB", 30, False, False)
    fixo = fonte.render(">", True, (255, 255, 255))
    screen_menu.blit(fixo, ((a/2)+100, (l/2)+35))
def selecao():
    global menu_selecao
    if (menu_selecao == 1):
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("INICIAR", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a/2)+215, (l/2)+35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        configuracao = fonte.render("CONFIGURAÇÔES", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 75))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        creditos = fonte.render("CRÉDITOS", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + 215, (l / 2) + 105))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        sair = fonte.render("SAIR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 135))

    if (menu_selecao == 2):
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("INICIAR", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) + 5))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        configuracao = fonte.render("CONFIGURAÇÔES", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        creditos = fonte.render("CRÉDITOS", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + 215, (l / 2) + 75))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        sair = fonte.render("SAIR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 105))

    if (menu_selecao == 3):
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("INICIAR", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) + -25))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        configuracao = fonte.render("CONFIGURAÇÔES", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 5))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        creditos = fonte.render("CRÉDITOS", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + 215, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        sair = fonte.render("SAIR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 75))

    if (menu_selecao == 4):
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("INICIAR", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) - 55))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        configuracao = fonte.render("CONFIGURAÇÔES", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) - 25))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        creditos = fonte.render("CRÉDITOS", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + 215, (l / 2) + 5))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        sair = fonte.render("SAIR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 35))

    if menu_selecao == 5:
        menu_selecao = 4
    if menu_selecao <= 0:
        menu_selecao = 1
    if menu_selecao == 6:
        menu_selecao = 1
    if menu_selecao == 96:
        menu_selecao = 1
    if menu_selecao == 95:
        menu_selecao = 1
    if menu_selecao == 94:
        menu_selecao = 1
    if menu_selecao == 93:
        menu_selecao = 1
    if menu_selecao == 92:
        menu_selecao = 1
    if menu_selecao == 91:
        menu_selecao = 1
    #menu_personagens
    if (menu_selecao == 11):
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        Jogo(screen)
    #configurações
    if menu_selecao == 12:
        menu_selecao = 200
    if menu_selecao == 200:
        pygame.mixer.music.unpause()
        #screen_menu.fill((255, 255, 255))
        screen.blit(fundoMenu, (0, 0))
        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("SOM", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("ON/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 265, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("OFF/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 305, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        configuracao = fonte.render("ALIASING", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 75))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        sair = fonte.render("VOLTAR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 105))

    if menu_selecao == 210:
        pygame.mixer.music.unpause()
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("SOM", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("ON/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 265, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("OFF/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 292, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        configuracao = fonte.render("ALIASING", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 75))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        sair = fonte.render("VOLTAR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 105))

    if menu_selecao == 220:
        menu_selecao = 200
    if menu_selecao == 249:
        menu_selecao = 200
    '''antialiasing'''
    if menu_selecao == 201:
        menu_selecao = 250
    if menu_selecao == 211:
        menu_selecao = 250
    if menu_selecao == 250:
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("SOM", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) + 5))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("ON/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 310, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("OFF/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 250, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        configuracao = fonte.render("ALIASING", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        sair = fonte.render("VOLTAR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 75))

    if menu_selecao == 260:
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("SOM", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) + 5))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("ON/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 310, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        iniciar = fonte.render("OFF/", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 337, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        configuracao = fonte.render("ALIASING", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 35))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        sair = fonte.render("VOLTAR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 75))
    #voltar
    if menu_selecao == 251:
        menu_selecao = 280
    if menu_selecao == 261:
        menu_selecao = 280
    if menu_selecao == 279:
        menu_selecao = 250
    if menu_selecao == 290:
        menu_selecao = 2
    if menu_selecao == 281:
        menu_selecao = 280
    if menu_selecao == 199:
        menu_selecao = 200
    if menu_selecao == 280:
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        iniciar = fonte.render("SOM", True, (255, 255, 255))
        fundoMenu.blit(iniciar, ((a / 2) + 215, (l / 2) + -25))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        configuracao = fonte.render("ALIASING", True, (255, 255, 255))
        fundoMenu.blit(configuracao, ((a / 2) + 215, (l / 2) + 5))

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        sair = fonte.render("VOLTAR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 215, (l / 2) + 35))

    if menu_selecao == 13:
        menu_selecao = 300
    if menu_selecao == 300:
        screen.blit(fundoMenu, (0, 0))
        #screen_menu.fill((255, 255, 255))
        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        creditos = fonte.render("PRODUZIDO POR:", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + -65, (l / 2)))

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        creditos = fonte.render("MAYCON R SANTANA", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + -65, (l / 2)) + 40)

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        creditos = fonte.render("KELVIN HAMSTER", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + -65, (l / 2)) + 70)

        fonte = pygame.font.SysFont("Agency FB", 20, False, False)
        creditos = fonte.render("UPE - ENG. SOFTWARE", True, (255, 255, 255))
        fundoMenu.blit(creditos, ((a / 2) + -65, (l / 2)) + 100)

        fonte = pygame.font.SysFont("Agency FB", 30, False, False)
        sair = fonte.render("VOLTAR", True, (255, 255, 255))
        fundoMenu.blit(sair, ((a / 2) + 115, (l / 2) + 35))

    if menu_selecao == 310:
        menu_selecao = 3
    if menu_selecao == 301:
        menu_selecao = 300
    if menu_selecao == 299:
        menu_selecao = 300
    if menu_selecao == 14:
        exit()
menu_selecao = 1

while (True): #Exibir os menus e movimentar a seleção

    fixo()
    #screen.blit(screen_menu, (0,0))
    screen.blit(fundoMenu, (0,0))
    pygame.display.update()
    pygame.display.flip()
    selecao()
    for e in pygame.event.get():
        if (e.type == QUIT):
            exit()
        if (e.type == KEYDOWN):
            if (e.key == K_DOWN):
                menu_selecao = menu_selecao+1
            if (e.key == K_UP):
                menu_selecao = menu_selecao-1
            if (e.key == K_RETURN):
                menu_selecao = menu_selecao+10
            if (e.key == K_ESCAPE):
                menu_selecao = menu_selecao-10


