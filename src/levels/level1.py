import pygame
from level import Level
from platforms import Platform
from characters.basic_enemy import Basic_enemy
from utils import *

class Level1_level(Level):
	

	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)
		
		#enemies = [[40, 40, 0, 0, 'Basic_enemy', 0],
		#		[40, 40, 0, 0, 'Basic_enemy', 1]]

		self.set_background_image('tutorial_background.png')
		self.parse_map('level1_map.txt')
		