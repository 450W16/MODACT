import pygame
from enemy import Enemy

class Wolf(Enemy)

	def __init__(self, width, height):
		Enemy.__init__(self, width, height)
		self.platform = None
		self.dir = 'R'
		self.speed = 2

	def update(self):
		if self.dir == 'R':
			self.rect.x += self.speed
			if self.rect.right > self.platform.rect.right:
				self.dir = 'L'
		else:
			self.rect.x -= self.speed
			if self.rect.left < self.platform.rect.left:
				self.dir = 'R'
