import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
from directions import Directions
from utils import *

class Monkey(Enemy):
	"""Monkey Enemy."""
	
	def __init__(self, width, height, x, y):
		Enemy.__init__(self, width, height, x, y)
		self.dir = 'R'
		self.speed = 2
		
		# initialize sprite lists
		ss = SpriteSheet(path.join(get_art_dir(), 'Monkey', 'Monkey_spritesheet.png'), 7)
		self.sprites_walk_left = ss.get_sprites(size=(45, 45))
		self.sprites_walk_right = [pygame.transform.flip(s, True, False) for s in self.sprites_walk_left]
		self.curr_sprite_index = 0
		
		self.image = self.sprites_walk_right[0]
		self.rect = self.image.get_rect()
		self.rect.x = width
		self.rect.y = height

	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
				
		return ret

	def update(self, c):
		if self.dir == 'R':
			self.rect.x += self.speed
			if self.rect.right > self.platform.rect.right:
				self.dir = 'L'
		else:
			self.rect.x -= self.speed
			if self.rect.left < self.platform.rect.left:
				self.dir = 'R'
		# Implement throw after aggro
