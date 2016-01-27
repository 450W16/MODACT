#!/bin/python
import pygame
from utils import *
from levels.tutorial_level import Tutorial_level
from characters.tracy import Tracy
from characters.biggie import Biggie
from levels.platforms import Platform


class Control(object):

	def __init__(self, screen):
		# instanciate players and their size
		self.player = Tracy(300, SCREEN_HEIGHT)
		self.AI = Biggie(200, SCREEN_HEIGHT)

		self.screen = screen

		# create sprite grouping for active sprites
		self.active_sprites = pygame.sprite.Group()
		self.active_sprites.add(self.player)
		self.active_sprites.add(self.AI)
		# which is active
		self.ACTIVE = self.player

		# create level and list of levels
		self.lvl_list = [Tutorial_level(self.player, self.AI)]
		self.lvl_num = 0
		self.lvl_current = self.lvl_list[self.lvl_num]
		self.player.level = self.lvl_current
		self.AI.level = self.lvl_current

		# some initialization for game loop
		self.done = False
		self.clock=pygame.time.Clock()

	def main_loop(self):
		while not self.done:
			for event in pygame.event.get()	:
				if event.type == pygame.QUIT:
					self.done = True

				# switch players (should be function?)
				pressed = pygame.key.get_pressed()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.player.move_left()
					if event.key == pygame.K_RIGHT:
						self.player.move_right()
					if event.key == pygame.K_SPACE:
						self.player.jump()
					else:
						k = self.player.checkAbility(event.key)
						if k is not None:
							k.cast(self)


				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT and self.player.delta_x < 0:
						self.player.stop()
					if event.key == pygame.K_RIGHT and self.player.delta_x > 0:
						self.player.stop()
			
			#update player
			self.active_sprites.update()

			# update level
			self.lvl_current.update()

			# scrolling
		

			# draw
			self.lvl_current.draw(self.screen)
			self.active_sprites.draw(self.screen)
			
			#FPS		
			self.clock.tick(60)
			
			#refresh screen
			pygame.display.flip()

def main():

	# initialize pygame
	pygame.init()

	# initialize screen
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("This is a game... or is it")

	Control(screen).main_loop()
	pygame.quit()

if __name__ == "__main__":
	main()
