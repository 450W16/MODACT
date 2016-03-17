import pygame
from enemy import Enemy

class Wolf(Enemy):

	def __init__(self, width, height, x, y):
		Enemy.__init__(self, width, height, x, y)
		self.dir = 'R'
		self.speed = 2

	def update(self, c):
		super(Wolf, self).update(c)
