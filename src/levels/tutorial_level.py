import pygame
from level import Level
from platforms import Platform
from characters.basic_enemy import Basic_enemy
from utils import *

class Tutorial_level(Level):
	

	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)
		
		#enemies = [[40, 40, 0, 0, 'Basic_enemy', 0],
		#		[40, 40, 0, 0, 'Basic_enemy', 1]]

		self.set_background_image('background.png')
		self.parse_map('tutorial_map.txt')
		
		"""
		for enemy in enemies:
			if enemy[4] == 'Basic_enemy':
				baddie = Basic_enemy(enemy[0], enemy[1])
				baddie.rect.x = self.platform_list.sprites()[enemy[5]].rect.x
				baddie.rect.y = self.platform_list.sprites()[enemy[5]].rect.y - enemy[1]
				baddie.platform = self.platform_list.sprites()[enemy[5]]
				self.enemy_list.add(baddie)
		"""