# AULA 1 - PYGAME
# LUCAS KPNZ

import pygame
from pygame.locals import *

pygame.init()

cor_preta = (0,0,0)

tela = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Teste")

player1_x = 100
player1_y = 100
player1_velocidade = 10

player2_x = 1180
player2_y = 100
player2_velocidade = 10

player1 = pygame.Surface((25,100))
player2 = pygame.Surface((25,100))

player1.fill(cor_preta)
player2.fill(cor_preta)

relogio = pygame.time.Clock()

while True:
	relogio.tick(30)
	tela.fill((255,255,255))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()
	
	key = pygame.key.get_pressed()
	if key[K_w] and player1_y > 0:
		player1_y -= player1_velocidade
	if key[K_s] and player1_y+100 < 720:
		player1_y += player1_velocidade
		
	if key[K_UP] and player2_y > 0:
		player2_y -= player2_velocidade
	if key[K_DOWN] and player2_y+100 < 720:
		player2_y += player2_velocidade
		
	tela.blit(player1, (player1_x,player1_y))
	tela.blit(player2, (player2_x,player2_y))
	pygame.display.update()
