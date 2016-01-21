import pygame
from player import Player
from utils import *

class Tracy(Player):
	
	def __init__(self):
		Player.__init__(self)
		
	def jump(self):
		print "tracy jump"
		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, 				self.level.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		if len(platform_collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.delta_y = -15
