import pygame

class Personagem:

    def __init__(self,arquivo_imagem,largura_imagem, altura_imagem,x_inicial,y_inicial): #função de construtor
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura)) #tranformando o tamanho da imagem

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.mascara = pygame.mask.from_surface (self.imagem)

    def desenhar (self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))

    def movimentar_via_setas(self):

        teclas = pygame.key.get_pressed()
        if teclas [pygame.K_RIGHT]: #direita
            if self.pos_x < 800-self.largura :
                self.pos_x = self.pos_x + 5 

        if teclas [pygame.K_LEFT]:
            if self.pos_x > 0 :
                self.pos_x = self.pos_x - 5 #esquerda

        if teclas [pygame.K_UP]:
            if self.pos_y > 0 :
                self.pos_y = self.pos_y - 5 #cima

        if teclas [pygame.K_DOWN]:
            if self.pos_y < 500-self.largura :
                self.pos_y = self.pos_y + 5 #baixo