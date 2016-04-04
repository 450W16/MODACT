import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
from directions import Directions
from banana import Banana
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
		self.image = self.sprites_walk_right[0]

		self.aggroRange = 200

		self.cooldown = 2000
		self.last = pygame.time.get_ticks()

	def jump(self, c):
		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, c.lvl_current.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		if len(platform_collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.delta_y = -15

	def gravity(self):
		if self.delta_y == 0:
			self.delta_y = 0.5
		else:
			self.delta_y += 0.5

	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
				
		return ret

	def update(self, c):
		self.gravity()
		if self.checkAggro(c, False):
			self.jump(c)

			# collision detection in y
			# check first so mob is positioned properly on top of platform
			self.rect.y += self.delta_y
			collide_list = pygame.sprite.spritecollide(self, c.lvl_current.platform_list, False)
			for platform in collide_list:
				if self.delta_y > 0:
					self.rect.bottom = platform.rect.top
				elif self.delta_y < 0:
					self.rect.top = platform.rect.bottom
				self.delta_y = 0

			now = pygame.time.get_ticks()
			if now - self.last >= self.cooldown:
				self.last = now
				b = Banana(10, 10, self.rect.x, self.rect.bottom, self)
				c.lvl_current.enemy_list.add(b)

		else:
			super(Monkey, self).update(c)
