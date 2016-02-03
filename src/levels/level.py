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
		dir = path.dirname(__file__)
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		self.AI = AI
		
		terrain1 = pygame.image.load(dir+"\\..\\..\\assets\\art\\terrain1.png")
		terrain2 = pygame.image.load(dir+"\\..\\..\\assets\\art\\terrain2.png")
		terrain3 = pygame.image.load(dir+"\\..\\..\\assets\\art\\terrain3.png")
		rock = pygame.image.load(dir+"\\..\\..\\assets\\art\\rockpixel_1.png")
		self.mapdict = {
			"B": terrain3,
			"G": terrain1,
			"g": terrain2,
			"#": rock
		}
		
		self.background_image = pygame.image.load(dir+"\\..\\..\\assets\\art\\background.png").convert()
		#self.background_position = pygame.Rect(0,0,0,0)
		
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen, camera):
		#TODO scrolling background
		screen.blit(self.background_image, camera.applyCam(self.background_image))

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
						platform.image = self.mapdict[block]
						self.platform_list.add(platform)
					x += BLOCK_WIDTH
				x = 0
				y += BLOCK_HEIGHT
				