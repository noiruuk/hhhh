import pygame
import random
import sys

from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)

pygame.init()

width = 800
height = 600

red = (255,0,0)
blue = (0,255,0)
background_color = (0,0,0)

speed = 10

player_size = 50
xpos = width/2
ypos = height - 2*player_size
player_pos = [xpos,ypos]

enemy_size = 50
enemy_pos = [random.randint(0,width-enemy_size),0]

screen = pygame.display.set_mode((width,height))

game_over = False

clock = pygame.time.Clock()

def detect_collision(player_pos,enemy_pos):
	# e1____e2
	# |      |
	# |      |
	# e3____e4
	#
	#    p1____p2
	#    |      |
	#    |      |
	#    p3____p4

	p1x = player_pos[0]
	p1y = player_pos[1]
	p2x = p1x + player_size
	p2y = p1y
	p3x = p1x
	p3y = p1y + player_size
	p4x = p2x
	p4y = p3y

	e1x = enemy_pos[0]
	e1y = enemy_pos[1]
	e2x = e1x + enemy_size
	e2y = e1y
	e3x = e1x
	e3y = e1y + enemy_size
	e4x = e2x
	e4y = e3y

	if (p1x >= e1x and p1x <= e2x and p1y >= e1y and p1y <= e3y) or \
	   (p2x >= e1x and p2x <= e2x and p2y >= e1y and p2y <= e3y) or \
	   (p3x >= e1x and p3x <= e2x and p3y >= e1y and p3y <= e3y) or \
	   (p4x >= e1x and p4x <= e2x and p4y >= e1y and p4y <= e3y):
	   return True
	return False


while not game_over:

	for event in pygame.event.get():
		#print(event)

		if event.type == QUIT:
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				game_over = True

			x = player_pos[0]
			y = player_pos[1]

			if event.key == K_LEFT:
				x -= player_size
			elif event.key == K_RIGHT:
				x += player_size

			player_pos = [x,y]
	screen.fill(background_color)

	if enemy_pos[1] >= 0 and enemy_pos[1] < height:
		enemy_pos[1] += speed
	else:
		enemy_pos[0] = random.randint(0,width-enemy_size)
		enemy_pos[1] = 0

	if detect_collision(player_pos,enemy_pos):
		print("COLLISION")
		game_over = True

	pygame.draw.rect(screen,blue,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))
	pygame.draw.rect(screen,red,(player_pos[0],player_pos[1],player_size,player_size))

	clock.tick(20)
	pygame.display.update()
