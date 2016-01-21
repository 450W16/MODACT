import pygame
from level import Level
from platforms import Platform

class Tutorial_level(Level):
	
	def __init__(self, player, AI):
		Level.__init__(self,player, AI)
		
		# an array of platforms
		level = [[210, 70, 500, 500],
			 [210, 70, 200, 400]]

		for platform in level:
			plat = Platform(platform[0], platform[1])
			plat.rect.x = platform[2]
			plat.rect.y = platform[3]
			self.platform_list.add(plat)
	
	
