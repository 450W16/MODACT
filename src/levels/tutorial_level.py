import pygame
from level import Level
from platforms import Platform
from characters.basic_enemy import Basic_enemy
from utils import *

class Tutorial_level(Level):
	
	# map tile textures
	BROWN = (153, 76, 0)
	GREEN = (0, 255, 0)
	GREY = (84, 84, 84)
	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)
		
		mapdict = {
			"B": self.BROWN,
			"G": self.GREEN,
			"#": self.GREY
		}
		
		map = [
			"                                                                       ",
			"                                                                       ",
			"                                                                       ",
			"                                                                       ",
			"                                                                       ",
			"                                                                       ",
			"                                                                       ",
			"                             GGGGGGGGGGG     GG                        ",
			"                             GGGGGGGGGGG     GGG                       ",
			"                             BBBBBBBBBBB     GGGG                      ",
			"                                  G          GGGGG                     ",
			"                                  G          GGGGGG                    ",
			"                                  G          GGGGGGG                   ",
			"                                  G          GGGGGGGG                  ",
			"                 ###              G          GGGGGGGGG                 ",
			"      ###        ###              G          GGGGGGGGGG                ",
			"GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
			"GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
			"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
		]
		
		#enemies = [[40, 40, 0, 0, 'Basic_enemy', 0],
		#		[40, 40, 0, 0, 'Basic_enemy', 1]]

		x = y = 0
		for row in map:
			for block in row:
				if block != " ":
					platform = Platform(x, y)
					platform.image.fill(mapdict[block])
					self.platform_list.add(platform)
				x += PLATFORM_WIDTH
			x = 0
			y += PLATFORM_HEIGHT
				
		
		for enemy in enemies:
			if enemy[4] == 'Basic_enemy':
				baddie = Basic_enemy(enemy[0], enemy[1])
				baddie.rect.x = self.platform_list.sprites()[enemy[5]].rect.x
				baddie.rect.y = self.platform_list.sprites()[enemy[5]].rect.y - enemy[1]
				baddie.platform = self.platform_list.sprites()[enemy[5]]
				self.enemy_list.add(baddie)
	
