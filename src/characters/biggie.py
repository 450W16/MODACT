import pygame
from player import Player
from abilities.ladder import Ladder
from abilities.bridge import *
from abilities.revert import Revert
from utils import *

# Default abilities: Ladder, Bridge, Reverts
class Biggie(Player):
	
	def __init__(self, x, y):
		Player.__init__(self, x, y)

		# initialize avitar (will replace with sprites later)
		self.image = pygame.Surface([BIGGIE_WIDTH, BIGGIE_HEIGHT])
		self.image.fill((0, 0, 255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		ladder = Ladder()
		self.abilities[ladder.getKey()] = ladder
		revert = Revert()
		self.abilities[revert.getKey()] = revert
		bridge = Bridge()
		self.abilities[bridge.getKey()] = bridge
		self.status = Transformed.Default
		
	def jump(self):

		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		# will have to change if we change ground
		if len(platform_collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.delta_y = -20
		
