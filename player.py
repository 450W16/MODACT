# player class

import pygame
import utils

class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()

		self.delta_x = 0
		self.delta_y = 0
		
		self.HP = utils.PLAYER_HEALTH
