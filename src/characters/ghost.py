import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
from utils import *

class Ghost(Enemy):
	"""Ghost Enemy."""
	
	def __init__(self, width, height, x, y):
		Enemy.__init__(self, width, height, x, y)
		self.dir = 'R'
		self.speed = 1
		
		# initialize sprite lists
		ss = SpriteSheet(path.join(get_art_dir(), 'Ghost', 'Ghost_spritesheet.png'), 12)
		self.sprites_walk_left = ss.get_sprites(size=(29, 43))
		self.sprites_walk_right = [pygame.transform.flip(s, True, False) for s in self.sprites_walk_left]
		self.curr_sprite_index = 0
		
		self.image = self.sprites_walk_right[0]

	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
				
		return ret

	def update(self, c):
		super(Ghost, self).update(c)
