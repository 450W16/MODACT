import pygame
from utils import *

class MovingPlatform(pygame.sprite.Sprite):
	
	change_x = 1
	change_y = 1
	
	boundary_top = 0
	boundary_bottom = 0
	boundary_left = 0
	boundary_right = 0
	
	def __init__(self, player, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width, height))
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.boundary_left = self.rect.left
		self.set_hor_move_amount(2)
		self.boundary_bottom = self.rect.bottom
		self.set_vert_move_amount(2)
		
		self.player = player
	
	def update(self):
		pass
		
	def set_hor_move_amount(self, numblocks):
		"""Up/down movement platforms start from left position"""
		self.boundary_right = self.rect.right + (self.rect.width * numblocks)
		
	def set_vert_move_amount(self, numblocks):
		"""Up/down movement platforms start from bottom position"""
		self.boundary_top = self.rect.top - (self.rect.height * numblocks)
		