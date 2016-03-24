import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
from directions import Directions
from utils import *

class Wolf(Enemy):
	"""Wolf Enemy."""
	
	def __init__(self, width, height, x, y):
		Enemy.__init__(self, width, height, x, y)
		self.dir = 'R'
		self.speed = 2
		
		# initialize sprite lists
		ss = SpriteSheet(path.join(get_art_dir(), 'Wolf', 'Wolf_spritesheet.png'), 6)
		self.sprites_walk_left = ss.get_sprites(size=(80, 41))
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
		super(Wolf, self).update(c)

