import pygame
from projectile import Projectile

class Banana(Projectile):

	def __init__(self, width, height, x, y):
		Projectile.__init__(self, width, height, x, y)
		self.speed = 1