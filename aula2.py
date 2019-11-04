# coding: utf-8
# AULA 1 - PYGAME
# LUCAS KPNZ

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

cor_preta = (0,0,0)

tela = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Teste")

player1_x = 100
player1_y = 100
player1_velocidade = 10

player2_x = 1180
player2_y = 100
player2_velocidade = 10

bola_x = 640
bola_y = 360
bola_velocidade = 5
bola_direcaox = 1
bola_direcaoy = 1

player1 = pygame.Surface((25,100))
player2 = pygame.Surface((25,100))
bola = pygame.Surface((25,25))

player1.fill(cor_preta)
player2.fill(cor_preta)
bola.fill((255,0,0))

fonteVencedor = pygame.font.SysFont('Comic Sans MS', 50)

fonteVencedor2 = fonteVencedor.render("Vencedor eh o jogador 2", 1, (38,255,0))
fonteVencedor1 = fonteVencedor.render("Vencedor eh o jogador 1", 1, (38,255,0))

relogio = pygame.time.Clock()

while True:
	relogio.tick(30)
	tela.fill((255,255,255))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()
			
	bola_x += bola_velocidade*bola_direcaox
	bola_y += bola_velocidade*bola_direcaoy
	
	
	# Sistema de limitação do mapa
	if (bola_y >= 720-25):
		bola_direcaoy = bola_direcaoy*-1
	if (bola_y <= 0+25):
		bola_direcaoy = bola_direcaoy*-1
		
	# Sistema de colisão
	if ((player1_y <= bola_y <= player1_y+125)and(player1_x <= bola_x <= player1_x+25)):
		bola_direcaox = bola_direcaox*-1
	if ((player2_y <= bola_y <= player2_y+125)and(player2_x <= bola_x+25 <= player2_x+25)):
		bola_direcaox = bola_direcaox*-1
	
	if (bola_x < 90):
		tela.blit(fonteVencedor2, (0,0))
		print ("Vencedor jogador numero 2")

	if (bola_x > 1190):
		tela.blit(fonteVencedor1, (0,0))
		print ("Vencedor jogador numero 2")

	
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
	tela.blit(bola, (bola_x, bola_y))
	pygame.display.update()
