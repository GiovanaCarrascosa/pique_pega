import pygame
import random
from personagem import Personagem
from movimento import Obstaculo

pontuacao = 0
vida = 50
pygame.init()

tela = pygame.display.set_mode ((800,600)) 

tela.fill((185,0,0))

pygame.display.set_caption("A queda capilar") 

lista_cabelos = [
Obstaculo("imagens/cabelo cacheado.png", 100,60,-10),
Obstaculo("imagens/cabelo comprido.png", 90,110,-20),
Obstaculo("imagens/cabelo harry styles.png", 80,70,-30),
Obstaculo("imagens/cabelo preto.png", 80,70,-25),
Obstaculo("imagens/cabelo loiro.png", 80,70,-15),
Obstaculo("imagens/cabelo laranja.png", 80,60,-17),
Obstaculo("imagens/topete menor.png", 80,70,-19),
Obstaculo("imagens/cabelo claro comprido.png", 90,110,-20),
]

lista_bomba = [
Obstaculo("imagens/secador.png", 80,70,-19),
Obstaculo("imagens/creme.png", 80,70,-19),
Obstaculo("imagens/maquininha.png", 80,70,-19),
Obstaculo("imagens/tesoura.png", 80,70,-19),
Obstaculo("imagens/secador.png", 80,70,-19),
]


    
calvo = Personagem ("imagens/personagem calvo.png",170,180,295,420)


CABELELEIRO = pygame.image.load("imagens/cabeleleiro.png") 
CABELELEIRO = pygame.transform.scale(CABELELEIRO,(800,600)) 



clock = pygame.time.Clock() 

rodando = True
while rodando: 
    for evento in pygame.event.get(): 
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Vc clicou!!")

        if evento.type == pygame.QUIT: 
            rodando = False 

    tela.blit(CABELELEIRO,(0,0))

    for movimento in lista_cabelos:
        movimento.correr()
        movimento.desenhar(tela)
    
    
        if calvo.mascara.overlap(movimento.mascara,(movimento.pos_x - calvo.pos_x, movimento.pos_y - calvo.pos_y)):
            movimento.pos_y = -20
            movimento.pos_x = random.randint(1, 750)
            pontuacao = pontuacao + 1
 
    teclas = pygame.key.get_pressed()

    if teclas [pygame.K_RIGHT]:
         if calvo.pos_x < 650 :
            calvo.pos_x = calvo.pos_x + 7 #mudar de posição sozinho

    if teclas [pygame.K_LEFT]:
        if calvo.pos_x > 0 :
            calvo.pos_x = calvo.pos_x - 7 #mudar de posição quando pressionar tecla para esquerda

    
    for movimento in lista_bomba:
        movimento.correr()
        movimento.desenhar(tela)

        if calvo.mascara.overlap(movimento.mascara,(movimento.pos_x - calvo.pos_x, movimento.pos_y - calvo.pos_y)):
            movimento.pos_y = -20
            movimento.pos_x = random.randint(1, 750)
            
            vida=vida-1
 
    
    calvo.desenhar(tela)

    fonte = pygame.font.SysFont("Berlin Sans FB Demi", 18, False,False)

    texto_pontuacao = fonte.render(f"Pontuação de pontos: {pontuacao}",True, (255,0,0)) 
    tela.blit(texto_pontuacao,(3,5)) 

    fonte = pygame.font.SysFont("Berlin Sans FB Demi", 18, False,False)

    texto_pontuacao = fonte.render(f"Vida: {vida}",True, (255,0,0)) 
    tela.blit(texto_pontuacao,(3,30)) 

    pygame.display.update() 

    clock.tick(60) 