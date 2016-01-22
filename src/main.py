#!/bin/python
import pygame
from utils import *
from tutorial_level import Tutorial_level
from tracy import Tracy
from biggie import Biggie
from platforms import Platform

def main():

	# initialize pygame
	pygame.init()

	# initialize screen
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("This is a game... or is it")

	# instanciate players and their size
	player = Tracy()
	player.rect.x = 300
	player.rect.y = SCREEN_HEIGHT - player.rect.height
	AI = Biggie()
	AI.rect.x = 200
	AI.rect.y = SCREEN_HEIGHT - AI.rect.height

	# create sprite grouping for active sprites
	active_sprites = pygame.sprite.Group()
	active_sprites.add(player)
	active_sprites.add(AI)
	# which is active
	ACTIVE = player

	# create level and list of levels
	lvl_list = []
	lvl_list.append( Tutorial_level(player, AI) ) # doesn't work for switching
	lvl_num = 0
	lvl_current = lvl_list[lvl_num]
	player.level = lvl_current
	AI.level = lvl_current

	# some initialization for game loop
	done = False
	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get()	:
			if event.type == pygame.QUIT:
				done = True

			# switch players (should be function?)
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_f]:
				# set change to 0 otherwise you get weird behaviour when
				# moving and switching
				player.delta_x = 0
				player, AI = AI, player
				ACTIVE = player

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.move_left()
				if event.key == pygame.K_RIGHT:
					player.move_right()
				if event.key == pygame.K_SPACE:
					player.jump()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.delta_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.delta_x > 0:
					player.stop()
		
		#update player
		active_sprites.update()

		# update level
		lvl_current.update()

		# draw
		lvl_current.draw(screen)
		active_sprites.draw(screen)
		
		#FPS		
		clock.tick(60)
		
		#refresh screen
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
