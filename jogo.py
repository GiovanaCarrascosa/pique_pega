import pygame
import random
from personagem import Personagem
from movimento import Obstaculo

fim = Personagem ("imagens/tela fim.png",800,600,0,0)
pontuacao = 0
vida = 10

pygame.mixer.init()
musica = pygame.mixer.Sound("taylor swift.mp3")
musica.set_volume(1.0)

pygame.init()

tela = pygame.display.set_mode ((800,600)) 

tela.fill((185,0,0))

pygame.display.set_caption("A queda capilar") 

lista_cabelos = [
Obstaculo("imagens/cabelo cacheado.png", 70,50,-10),
Obstaculo("imagens/cabelo comprido.png", 70,90,-20),
Obstaculo("imagens/cabelo harry styles.png", 70,60,-30),
Obstaculo("imagens/cabelo preto.png", 70,60,-25),
Obstaculo("imagens/cabelo loiro.png", 70,60,-15),
Obstaculo("imagens/cabelo laranja.png", 70,50,-17),
Obstaculo("imagens/topete menor.png", 70,60,-19),
Obstaculo("imagens/cabelo claro comprido.png", 70,90,-20),
]

lista_bomba = [
Obstaculo("imagens/secador.png", 70,60,-19),
Obstaculo("imagens/creme.png", 70,60,-19),
Obstaculo("imagens/maquininha.png", 70,60,-19),
Obstaculo("imagens/tesoura.png", 70,60,-19),
Obstaculo("imagens/secador.png", 70,60,-19),
]

calvo = Personagem ("imagens/personagem calvo.png",170,180,295,420)


CABELELEIRO = pygame.image.load("imagens/cabeleleiro.png") 
CABELELEIRO = pygame.transform.scale(CABELELEIRO,(800,600)) 


clock = pygame.time.Clock() 

rodando = True
while rodando: 
    for evento in pygame.event.get(): 
           
            if vida == 0:
                rodando = False
            else:
                calvo.movimentar_via_setas()
                calvo.desenhar(tela)

            if evento.type == pygame.QUIT: 
                rodando = False 

    tela.blit(CABELELEIRO,(0,0))

    calvo.movimentar_via_setas()
    calvo.desenhar(tela)
        

    for movimento in lista_cabelos:
            movimento.correr()
            movimento.desenhar(tela)
    
    
            if calvo.mascara.overlap(movimento.mascara,(movimento.pos_x - calvo.pos_x, movimento.pos_y - calvo.pos_y)):
                movimento.pos_y = -20
                movimento.pos_x = random.randint(1, 730)
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
 
    musica.play()

    fonte = pygame.font.SysFont("Berlin Sans FB Demi", 18, False,False)

    texto_pontuacao = fonte.render(f"Pontuação de pontos: {pontuacao}",True, (255,0,0)) 
    tela.blit(texto_pontuacao,(3,5)) 

    fonte = pygame.font.SysFont("Berlin Sans FB Demi", 18, False,False)

    texto_pontuacao = fonte.render(f"Vida: {vida}",True, (255,0,0)) 
    tela.blit(texto_pontuacao,(3,30)) 

    

    pygame.display.update() 

    clock.tick(60) 