import pygame
from utils import *

class Trigger(pygame.sprite.Sprite):

	def __init__(self, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):

		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((width, height))
		self.image.fill((255, 0, 0))
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x