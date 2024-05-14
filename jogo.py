import pygame
from personagem import Personagem

pygame.init()

tela = pygame.display.set_mode ((800,600)) 

tela.fill((185,0,0))

pygame.display.set_caption("A queda capilar") 



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
 
    teclas = pygame.key.get_pressed()

    if teclas [pygame.K_RIGHT]:
         if calvo.pos_x < 750 :
            calvo.pos_x = calvo.pos_x + 7 #mudar de posição sozinho

    if teclas [pygame.K_LEFT]:
        if calvo.pos_x > 0 :
            calvo.pos_x = calvo.pos_x - 7 #mudar de posição quando pressionar tecla para esquerda


    
    calvo.desenhar(tela)



    pygame.display.update() 

    clock.tick(60) 