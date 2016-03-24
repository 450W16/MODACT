import pygame
from level import Level
from platforms import Platform
from characters import *
from utils import *

def initGhost(width, height, x, y):
		return Ghost(width, height, x, y)

def initEnemy(level, baddie):
	level.enemy_list.add(baddie)
	
class Level1_level(Level):
	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)
		
		enemies = {
			'G': initGhost
		}
		
		
		self.parse_map('level1_map.txt', enemies, initEnemy)
		self.set_background_image('tutorial_background.png')
		self.music = 'levels/forest.mp3'
