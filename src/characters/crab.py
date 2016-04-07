import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
from directions import Directions
from utils import *

class Crab(Enemy):
	"""Crab Enemy."""
	
	def __init__(self, width, height, x, y):
		Enemy.__init__(self, 55, 25, x, y)
		self.dir = 'R'
		self.speed = 1
		
		# initialize sprite lists
		ss = SpriteSheet(path.join(get_art_dir(), 'Crab', 'Crab_spritesheet.png'), 4)
		self.sprites_walk_right = ss.get_sprites(size=(55, 25))
		self.sprites_walk_left = [pygame.transform.flip(s, True, False) for s in self.sprites_walk_right]
		self.image = self.sprites_walk_right[0]

	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
				
		return ret

	def update(self, c):
		super(Crab, self).update(c)
