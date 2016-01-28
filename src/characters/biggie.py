import pygame
from player import Player
from utils import *

class Biggie(Player):
	

	def __init__(self, x, y):
		Player.__init__(self, x, y)

		# initialize avitar (will replace with sprites later)
		self.image = pygame.Surface([BIGGIE_WIDTH, BIGGIE_HEIGHT])
		self.image.fill((0, 0, 255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def jump(self):

		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, 				self.level.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		# will have to change if we change ground
		if len(platform_collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.delta_y = -20
		
