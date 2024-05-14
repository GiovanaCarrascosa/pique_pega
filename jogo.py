import pygame

pygame.init()
tela = pygame.display.set_mode ((1000,700))
tela.fill ((185,0,0))

pygame.display.set_caption("A queda capilar")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

clock = pygame.time.Clock()

pygame.display.update()


clock.tick(60)