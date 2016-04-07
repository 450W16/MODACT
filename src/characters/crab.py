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
		self.radius = 100
		self.dist = 0
		
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

		self.update_sprites()
		self.gravity()

		
		if self.dir == "R":
			self.delta_x += self.speed
			self.dist += self.speed
			if self.dist >= self.radius:
				self.dir = "L"
				self.dist = 0
		else: # self.dir = "L"
			self.delta_x -= self.speed
			self.dist +- self.speed
			if self.dist >= self.radius:
				self.dir = "L"
				self.dist = 0

		pl = c.lvl_current.platform_list

		# collision detection in y
		# check first so mob is positioned properly on top of platform
		self.rect.y += self.delta_y
		collide_list = pygame.sprite.spritecollide(self, pl, False)
		for platform in collide_list:
			if self.delta_y > 0:
				self.rect.bottom = platform.rect.top
			elif self.delta_y < 0:
				self.rect.top = platform.rect.bottom
			self.delta_y = 0


		
		# collision detection in x
		# If collide with wall, reverse direction
		self.rect.x += self.delta_x
		collide_list = pygame.sprite.spritecollide(self, pl, False)
		for platform in collide_list:
			if self.delta_x > 0: # dir = "R"
				self.rect.right = platform.rect.left
				self.dir = "L"
			elif self.delta_x < 0: # dir = "L"
				self.rect.left = platform.rect.right
				self.dir = "R"
		self.delta_x = 0


