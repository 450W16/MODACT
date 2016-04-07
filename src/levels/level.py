import pygame
from os import path
from platforms import Platform
from triggers import Trigger
from wallTrigger import WallTrigger
from vine_trigger import VineTrigger
from moving_platformsLR import MplatformLR
from moving_platformsUD import MplatformUD
from vine import Vine
from utils import *

class Level():
	
	def __init__(self, player, AI):
		self.platform_list = pygame.sprite.Group()
		self.trigger_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.special_platforms = pygame.sprite.Group()
		self.vinetrigger_list = pygame.sprite.Group()
		self.wallTrigger_list = pygame.sprite.Group()
		self.title_list = []
		self.title_rect = pygame.Rect(20, 180, SCREEN_WIDTH//4, SCREEN_HEIGHT//4)
		self.load_rect = pygame.Rect(240, 290, 100, 50)
		self.player = player
		self.AI = AI
		self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.music = None
		self.music_is_playing = False
		self.level_width = 0
		self.level_height = 0
		self.ground_level = 0
		self.load_block = None

		grass = pygame.image.load(path.join(get_art_dir(), "terrain1.png"))
		dirt = pygame.image.load(path.join(get_art_dir(), "terrain2.png"))
		self.dirt_bottom = pygame.image.load(path.join(get_art_dir(), "terrain3.png"))
		rock1 = pygame.image.load(path.join(get_art_dir(), "rock1.png"))
		rock2 = pygame.image.load(path.join(get_art_dir(), "rock2.png"))
		rock3 = pygame.image.load(path.join(get_art_dir(), "rock3.png"))
		rock4 = pygame.image.load(path.join(get_art_dir(), "rock4.png"))
		rock5 = pygame.image.load(path.join(get_art_dir(), "rock5.png"))
		rock_leftend = pygame.image.load(path.join(get_art_dir(), "rock6.png"))
		rock_topend = pygame.image.load(path.join(get_art_dir(), "rock7.png"))
		rock_rightend = pygame.image.load(path.join(get_art_dir(), "rock8.png"))
		sandtop = pygame.image.load(path.join(get_art_dir(), "sand1.png"))
		sandmiddle = pygame.image.load(path.join(get_art_dir(), "sand2.png"))
		sandbottom = pygame.image.load(path.join(get_art_dir(), "sand3.png"))
		self.mapdict = {
			"g": grass,
			"D": dirt,
			"d": self.dirt_bottom,
			"1": rock1,
			"2": rock2,
			"3": rock3,
			"4": rock4,
			"5": rock5,
			"6": rock_leftend,
			"7": rock_topend,
			"8": rock_rightend,
			"a": sandtop,
			"s": sandmiddle,
			"b": sandbottom
		}
		
	def update(self, c):
		self.platform_list.update(c)
		self.trigger_list.update(c)
		self.enemy_list.update(c)
		self.vinetrigger_list.update(c)
		self.wallTrigger_list.update(c)
		if not self.music_is_playing:
			self.playMusic()
		if c.player.rect.top > self.level_height:
			c.player.dead = True
			#c.player.rect.x = self.Px
			#c.player.rect.y = self.Py
			#c.AI.rect.x = self.Ax
			#c.AI.rect.y = self.Ay
		if self.load_block:
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			if  c.camera.applyCam(self.load_rect).collidepoint(mouse) and click[0]:
				c.load()
		
	def draw(self, screen, camera):
		#TODO slower scrolling background
		screen.blit(self.background_image, camera.applyCam(self.background_image))
		if self.background_image.get_rect().right < self.level_width:
			rect = pygame.Rect(self.background_image.get_rect().right, self.background_image.get_rect().top, self.background_image.get_rect().width, self.background_image.get_rect().height)
			screen.blit(self.background_image, camera.applyCam(rect))
		#if self.background_image.get_rect().bottom < self.level_height:
		#	rect = pygame.Rect(self.background_image.get_rect().left, self.background_image.get_rect().bottom, self.background_image.get_rect().width, self.background_image.get_rect().height)
		#	screen.blit(self.background_image, camera.applyCam(rect))
		#if rect.y < self.level_height:
		#	rect2 = pygame.Rect(rect.left, rect.bottom, rect.width, rect.height)
		#	screen.blit(self.background_image, camera.applyCam(rect2)) 

		for plat in self.platform_list:
			screen.blit(plat.image, camera.applyCam(plat))

		for trig in self.trigger_list:
			screen.blit(trig.image, camera.applyCam(trig))

		for enemy in self.enemy_list:
			screen.blit(enemy.image, camera.applyCam(enemy))

		for title in self.title_list:
			screen.blit(title, camera.applyCam(self.title_rect))

		if self.load_block != None:
			screen.blit(self.load_block, camera.applyCam(self.load_rect))
			
		for vinetrigger in self.vinetrigger_list:
			screen.blit(vinetrigger.image, camera.applyCam(vinetrigger))

		for walltrigger in self.wallTrigger_list:
			screen.blit(walltrigger.image, camera.applyCam(walltrigger))
			
	def parse_map(self, filename, enemies, callback):
		with open(path.join(get_levels_dir(), filename), "r") as f:
			x = y = 0
			for line in f:
				for block in line.rstrip():
					if block != " ":
						#need a trigger block image
						if block in enemies:
							callback(self, enemies[block](40, 40, x, y))
						elif block == "E":
							trigger = Trigger(x, y)
							self.trigger_list.add(trigger)
						elif block == "w":
							walltrigger = WallTrigger(x, y)
							self.wallTrigger_list.add(walltrigger)
						elif block == "^":
							moving_platformsUD = MplatformUD(x, y)
							self.platform_list.add(moving_platformsUD)
						elif block == "v":
							vine = Vine(x, y)
							self.platform_list.add(vine)
						elif block == "V":
							vinetrigger = VineTrigger(x, y)
							self.vinetrigger_list.add(vinetrigger)
						elif block == ">":
							moving_platformsLR = MplatformLR(x, y)
							self.platform_list.add(moving_platformsLR)

						elif block == "P":
							self.Px = x
							self.Py = y 
						elif block == "A":
							self.Ax = x
							self.Ay = y 
						elif block == "y":
							self.ground_level = y
						else:
							platform = Platform(x, y)
							platform.image = self.mapdict[block]
							self.platform_list.add(platform)
					x += BLOCK_WIDTH

				if x > self.level_width:
					self.level_width = x
				x = 0
				y += BLOCK_HEIGHT

			self.level_height = y

				
	def set_background_image(self, filename):
		self.background_image = pygame.Surface((self.level_width, self.level_height))
		self.background_image = pygame.image.load(path.join(get_art_dir(), filename)).convert()
		

	def playMusic(self):
		if self.music != None:
			pygame.mixer.music.load(self.music)
			pygame.mixer.music.play(-1)
			self.music_is_playing = True
