import pygame
from directions import Directions
from projectile import Projectile
from spritesheet import SpriteSheet
from utils import *

class Banana(Projectile):

	def __init__(self, width, height, x, y, owner=None):
		Projectile.__init__(self, 25, 25, x, y)
		self.owner = owner
		self.speed = 1
		
		# initialize sprite lists
		ss = SpriteSheet(path.join(get_art_dir(), 'Monkey', 'Banana_spritesheet.png'), 8)
		self.sprites_throw_right = ss.get_sprites(size=(25, 25))
		self.sprites_throw_left = [pygame.transform.flip(s, True, False) for s in self.sprites_throw_right]

	def update(self, c):
		super(Banana, self).update(c)
		self.rect.y += self.speed
		collide_list = pygame.sprite.spritecollide(self, c.lvl_current.special_platforms, False)
		if len(collide_list) >= 1:
			self.kill()

	def get_sprites(self):
		# Default
		ret = self.sprites_throw_right
		
		if self.owner is not None:
			if self.owner.heading == Directions.Left:
				ret = self.sprites_throw_left
			elif self.owner.heading == Directions.Right:
				ret = self.sprites_throw_right
				
		return ret
