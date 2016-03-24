import pygame
from level import Level
from platforms import Platform
from characters.ghost import Ghost
from characters.spider import Spider
from utils import *

def initGhost(width, height, x, y):
	return Ghost(width, height, x, y)

def initSpider(width, height, x, y):
	return Spider(width, height, x, y)

def initEnemy(level, baddie):
	level.enemy_list.add(baddie)

class Tutorial_level(Level):

	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)

		enemies = {
			'G': initGhost,
			'S': initSpider
		}
		# enemies = {}

		
		self.parse_map('tutorial_map.txt', enemies, initEnemy)
		self.set_background_image('tutorial_background.png')
		
	
		
