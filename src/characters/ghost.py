import pygame
from enemy import Enemy

class Ghost(Enemy):

	def __init__(self, width, height, x, y):
		Enemy.__init__(self, width, height, x, y)
		self.dir = 'R'
		self.speed = 1

	def update(self, c):
		super(Ghost, self).update(c)
