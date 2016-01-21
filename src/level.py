import pygame

class Level():
	
	def __init__(self, player):
		
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen):
		#TODO draw background
		screen.fill((0,0,0))

		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)
		
