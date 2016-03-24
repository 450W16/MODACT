import pygame

class Projectile(pygame.sprite.Sprite):

	def __init__(self, width, height, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width, height))
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, c):
		pass