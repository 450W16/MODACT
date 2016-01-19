# player class

import pygame
from utils import *

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# change in x and y
		self.delta_x = 0
		self.delta_y = 0

		# player hitpoints
		self.HP = PLAYER_HEALTH

		# initialize avitar (will replace with sprites later)
		self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
		self.image.fill((0, 0, 255))
		self.rect = self.image.get_rect()

	def update(self):
		# update movements, gravity, animation, etc.
		self.gravity()
		self.rect.x += self.delta_x
		self.rect.y += self.delta_y
		
	def gravity(self):
		if self.delta_y == 0:
			self.delta_y = 1
		else:
			self.delta_y += 1

		# check if we're on the ground
		if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.delta_y >= 0:
			self.delta_y = 0
			self.rect.y = SCREEN_HEIGHT - self.rect.height
	
	def move_left(self):
		self.delta_x = -5

	def move_right(self):
		self.delta_x = 5

	def jump(self):
		pass

	def stop(self):
		self.delta_x = 0

		
