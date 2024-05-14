import pygame
from personagem import Personagem
from movimento import Obstaculo

pontuacao = 0
pygame.init()

tela = pygame.display.set_mode ((800,600)) 

tela.fill((185,0,0))

pygame.display.set_caption("A queda capilar") 

lista_cabelos = [
Obstaculo("imagens/cabelo cacheado.png", 140,90,-10),
Obstaculo("imagens/cabelo comprido.png", 110,130,-20),
Obstaculo("imagens/cabelo harry styles.png", 100,90,-30),
Obstaculo("imagens/cabelo preto.png", 100,90,-25),
Obstaculo("imagens/cabelo loiro.png", 100,90,-15),
Obstaculo("imagens/cabelo laranja.png", 120,90,-17),
Obstaculo("imagens/topete menor.png", 100,90,-19),
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
       
            pontuacao = pontuacao + 1
 
    teclas = pygame.key.get_pressed()

    if teclas [pygame.K_RIGHT]:
         if calvo.pos_x < 650 :
            calvo.pos_x = calvo.pos_x + 7 #mudar de posição sozinho

    if teclas [pygame.K_LEFT]:
        if calvo.pos_x > 0 :
            calvo.pos_x = calvo.pos_x - 7 #mudar de posição quando pressionar tecla para esquerda

    

    
    calvo.desenhar(tela)

    fonte = pygame.font.SysFont("Berlin Sans FB Demi", 18, False,False)

    texto_pontuacao = fonte.render(f"Pontuação de pontos: {pontuacao}",True, (255,0,0)) 
    tela.blit(texto_pontuacao,(3,5)) 

    pygame.display.update() 

    clock.tick(60) 