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
		#self.width = SCREEN_WIDTH
		#self.height = SCREEN_HEIGHT


