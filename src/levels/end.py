import pygame
from level import Level
from platforms import Platform
from utils import *

def initEnemy(level, baddie):
	level.enemy_list.add(baddie)

class End_level(Level):
	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)

		enemies = {
	
		}

		
		self.parse_map('end.txt', enemies, initEnemy)
		self.set_background_image('level2_background.gif')

		self.background_image = pygame.transform.scale(self.background_image, (self.level_width, self.level_height - BLOCK_HEIGHT*5))
	
		myFont = pygame.font.SysFont("monospace", 100)
		title = myFont.render("YOUR A WINNER", 1, (255,255,255))
		self.title_list.append(title)

		self.music = 'levels/forest.mp3'

		

