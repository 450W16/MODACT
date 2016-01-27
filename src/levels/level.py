import pygame
from utils import *

class Level():
	
	def __init__(self, player, AI):
		
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		self.AI = AI

		self.totalShift = 0
		
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen):
		#TODO draw background
		screen.fill((0,0,0))

		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

	def shift(self, delta_x):
		
		self.totalShift += delta_x

		for platform in self.platform_list:
			platform.rect.x += delta_x

		for enemy in self.enemy_list:
			enemy.rect.x += delta_x
