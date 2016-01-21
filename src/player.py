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

		#players level
		self.level = None

	def update(self):
		# update movements, gravity, animation, etc.
		self.gravity()

		self.rect.x += self.delta_x
		# collision detection in x
		collide_list = pygame.sprite.spritecollide(self, 
				self.level.platform_list, False)
		for platform in collide_list:
			if self.delta_x > 0:
				self.rect.right = platform.rect.left
			elif self.delta_x < 0:
				self.rect.left = platform.rect.right

		self.rect.y += self.delta_y
		# collision detection in y
		collide_list = pygame.sprite.spritecollide(self, 
				self.level.platform_list, False)
		for platform in collide_list:
			if self.delta_y > 0:
				self.rect.bottom = platform.rect.top
			elif self.delta_y < 0:
				self.rect.top = platform.rect.bottom
			self.delta_y = 0
		
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

		
