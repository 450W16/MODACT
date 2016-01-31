import pygame
from os import path
from platforms import Platform
from utils import *

class Level():
	
	# map tile textures
	BROWN = (153, 76, 0)
	GREEN = (0, 255, 0)
	GREY = (84, 84, 84)
	
	def __init__(self, player, AI):
		
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		self.AI = AI
		self.mapdict = {
			"B": self.BROWN,
			"G": self.GREEN,
			"#": self.GREY
		}
		
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen, camera):
		#TODO draw background
		screen.fill((0,0,0))

		for plat in self.platform_list:
			screen.blit(plat.image, camera.applyCam(plat))

		for enemy in self.enemy_list:
			screen.blit(enemy.image, camera.applyCam(enemy))
			
	def parse_map(self, filepath):
		dir = path.dirname(__file__)
		with open(path.join(dir, filepath), "r") as f:
			x = y = 0
			for line in f:
				for block in line.rstrip():
					if block != " ":
						platform = Platform(x, y)
						platform.image.fill(self.mapdict[block])
						self.platform_list.add(platform)
					x += BLOCK_WIDTH
				x = 0
				y += BLOCK_HEIGHT
				