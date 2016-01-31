import pygame
from utils import *

class Platform(pygame.sprite.Sprite):

	def __init__(self, x, y, width=32, height=32):

		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y