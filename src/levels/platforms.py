import pygame
from utils import *

class Platform(pygame.sprite.Sprite):

	def __init__(self, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):

		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((width, height))
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y