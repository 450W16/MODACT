import pygame
from os import path
from platforms import Platform
from triggers import Trigger 
from moving_platformsLR import MplatformLR
from moving_platformsUD import MplatformUD
from vine import Vine
from utils import *

class Level():
	
	def __init__(self, player, AI):
		self.platform_list = pygame.sprite.Group()
		self.trigger_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		self.AI = AI
		self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.music = None
		self.music_is_playing = False

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

	def update(self, c):
		self.platform_list.update()
		self.trigger_list.update()
		self.enemy_list.update(c)
		if not self.music_is_playing:
			self.playMusic()
		
	def draw(self, screen, camera):
		#TODO slower scrolling background
		screen.blit(self.background_image, camera.applyCam(self.background_image))
		if self.background_image.get_rect().right < LEVEL_WIDTH:
			rect = pygame.Rect(self.background_image.get_rect().right, self.background_image.get_rect().top, self.background_image.get_rect().width, self.background_image.get_rect().height)
			screen.blit(self.background_image, camera.applyCam(rect))

		for plat in self.platform_list:
			screen.blit(plat.image, camera.applyCam(plat))

		#for platUD in self.platform_listUD:
		#	screen.blit(platUD.image, camera.applyCam(platUD))

		#for platLR in self.platform_listLR:
		#	screen.blit(platLR.image, camera.applyCam(platLR))

		for trig in self.trigger_list:
			screen.blit(trig.image, camera.applyCam(trig))

		for enemy in self.enemy_list:
			screen.blit(enemy.image, camera.applyCam(enemy))
			
	def parse_map(self, filename, enemies, callback):
		with open(path.join(get_levels_dir(), filename), "r") as f:
			x = y = 0
			for line in f:
				for block in line.rstrip():
					if block != " ":
						#need a trigger block image
						if block == "E":
							trigger = Trigger(x, y)
							self.trigger_list.add(trigger)
						#need a vertically moving platform image
						elif block == "^":
							moving_platformsUD = MplatformUD(self.player, x, y)
							self.platform_list.add(moving_platformsUD)
						elif block == "v":
							vine = Vine(self.player, x, y)
							self.platform_list.add(vine)
						#need a horizontally moving platform image
						elif block == ">":
							moving_platformsLR = MplatformLR(self.player, x, y)
							self.platform_list.add(moving_platformsLR)
						elif block in enemies:
							callback(self, enemies[block](40, 40, x, y))
						else:
							platform = Platform(x, y)
							platform.image = self.mapdict[block]
							self.platform_list.add(platform)
					x += BLOCK_WIDTH
				x = 0
				y += BLOCK_HEIGHT
				
	def set_background_image(self, filename):
		self.background_image = pygame.image.load(path.join(get_art_dir(), filename)).convert()

	def playMusic(self):
		if self.music != None:
			pygame.mixer.music.load(self.music)
			pygame.mixer.music.play(-1)
			self.music_is_playing = True
