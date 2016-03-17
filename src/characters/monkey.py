import pygame
from enemy import Enemy

class Monkey(Enemy):

	def __init__(self, width, height, x, y):
		Enemy.__init__(self, width, height, x, y)
		self.dir = 'R'
		self.speed = 2

	def update(self, c):
		if self.checkAggro(c, False):
			# Throw
		else:
			super(Monkey, self).update(c)