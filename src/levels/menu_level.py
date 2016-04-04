import pygame
from level import Level
from platforms import Platform
from utils import *

def initEnemy(level, baddie):
	level.enemy_list.add(baddie)

class Menu_level(Level):
	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)

		enemies = {
	
		}

		
		self.parse_map('menu.txt', enemies, initEnemy)
		self.set_background_image('menu.png')

		self.background_image = pygame.transform.scale(self.background_image, (self.level_width, self.level_height - BLOCK_HEIGHT*5))
	
		myFont = pygame.font.SysFont("monospace", 100)
		title = myFont.render("Imaginary", 1, (255,255,255))
		self.title_list.append(title)

		# block for loading
		


