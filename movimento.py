import pygame
import random
class Obstaculo:
    def __init__(self,arquivo_imagem,largura_imagem, altura_imagem,x_inicial,y_inicial): #função de construtor
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura)) #tranformando o tamanho da imagem

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.pox_x = x_inicial
        self.pos_y - y_inicial

        self.velocidade = random.randint(3, 10)

        self.mascara = pygame.mask.from_surface (self.imagem)

    def correr(self):
            if self.pos_x <=-100 :
                 self.pos_x = 900
            self.pos_x = self.pos_x - self.velocidade

          


    def desenhar(self,tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))