import pygame
from player import Player
from utils import *

class Tracy(Player):
	
	def __init__(self, x, y):
		Player.__init__(self, x, y)

		# initialize avitar (will replace with sprites later)
		self.image = pygame.Surface([TRACY_WIDTH, TRACY_HEIGHT])
		self.image.fill((0, 0, 255))
		self.rect = self.image.get_rect()
		
	def jump(self):

		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, 				self.level.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		if len(platform_collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.delta_y = -15