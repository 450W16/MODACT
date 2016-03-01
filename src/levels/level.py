import pygame
from os import path
from platforms import Platform
from triggers import Trigger 
from utils import *

class Level():
	
	def __init__(self, player, AI):
		self.platform_list = pygame.sprite.Group()
		self.trigger_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		self.AI = AI
		self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		
		grass = pygame.image.load(path.join(get_art_dir(), "terrain1.png"))
		dirt = pygame.image.load(path.join(get_art_dir(), "terrain2.png"))
		dirt_bottom = pygame.image.load(path.join(get_art_dir(), "terrain3.png"))
		rock1 = pygame.image.load(path.join(get_art_dir(), "rock1.png"))
		rock2 = pygame.image.load(path.join(get_art_dir(), "rock2.png"))
		rock3 = pygame.image.load(path.join(get_art_dir(), "rock3.png"))
		rock4 = pygame.image.load(path.join(get_art_dir(), "rock4.png"))
		rock5 = pygame.image.load(path.join(get_art_dir(), "rock5.png"))
		rock_leftend = pygame.image.load(path.join(get_art_dir(), "rock6.png"))
		rock_topend = pygame.image.load(path.join(get_art_dir(), "rock7.png"))
		rock_rightend = pygame.image.load(path.join(get_art_dir(), "rock8.png"))
		self.mapdict = {
			"g": grass,
			"D": dirt,
			"d": dirt_bottom,
			"1": rock1,
			"2": rock2,
			"3": rock3,
			"4": rock4,
			"5": rock5,
			"6": rock_leftend,
			"7": rock_topend,
			"8": rock_rightend
		}
		
	def update(self):
		self.platform_list.update()
		self.trigger_list.update()
		self.enemy_list.update()

	def draw(self, screen, camera):
		#TODO slower scrolling background
		screen.blit(self.background_image, camera.applyCam(self.background_image))

		for plat in self.platform_list:
			screen.blit(plat.image, camera.applyCam(plat))

		for trig in self.trigger_list:
			screen.blit(trig.image, camera.applyCam(trig))

		for enemy in self.enemy_list:
			screen.blit(enemy.image, camera.applyCam(enemy))
			
	def parse_map(self, filename):
		with open(path.join(get_levels_dir(), filename), "r") as f:
			x = y = 0
			for line in f:
				for block in line.rstrip():
					if block != " ":
						platform = Platform(x, y)
						platform.image = self.mapdict[block]
						self.platform_list.add(platform)
						if block == "E":
							trigger = Trigger(x, y)
							self.trigger_list.add(trigger)
					x += BLOCK_WIDTH
				x = 0
				y += BLOCK_HEIGHT
				
	def set_background_image(self, filename):
		self.background_image = pygame.image.load(path.join(get_art_dir(), filename)).convert()
