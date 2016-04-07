import pygame
from spritesheet import SpriteSheet
from enemy import Enemy
from directions import Directions
from utils import *

class Spider(Enemy):

	def __init__(self, width, height, x, y):
		Enemy.__init__(self, width, height, x, y)
		self.dir = 'D'
		self.speed = 1
		
		# initialize sprite lists
		ss = SpriteSheet(path.join(get_art_dir(), 'Spider', 'Spider_spritesheet.png'), 4)
		self.sprites_walk_left = ss.get_sprites(size=(30, 20))
		self.sprites_walk_right = [pygame.transform.flip(s, True, False) for s in self.sprites_walk_left]
		self.image = self.sprites_walk_left[0]

	def update(self, c):
		# Always face the player
		if self.rect.x < c.player.rect.x:
			self.heading = Directions.Right
		else:
			self.heading = Directions.Left
			
		self.update_sprites()
		
		# Check aggro
		if not self.checkAggro(c, False):
			if self.dir == 'U':
				self.delta_y = -self.speed
			else:
				self.delta_y = self.speed
		else:
			dist =  c.player.rect.y - self.rect.y
			if dist > 0:
				self.dir == 'D'
				self.delta_y = self.speed
			else:
				self.dir == 'U'
				self.delta_y = -self.speed


		pl = c.lvl_current.platform_list

		# collision detection in y 
		self.rect.y += self.delta_y
		collide_list = pygame.sprite.spritecollide(self, pl, False)
		for platform in collide_list:
			if self.delta_y > 0:
				self.rect.bottom = platform.rect.top
				self.dir = "U"
			elif self.delta_y < 0:
				self.rect.top = platform.rect.bottom
				self.dir = "D"
			self.delta_y = 0

		# Move above top boundary
		if self.rect.top <= 0:
			self.rect.top = 0
			self.dir = "D"

		# collision detection in x
		# self.rect.x += self.delta_x
		# collide_list = pygame.sprite.spritecollide(self, pl, False)
		# for platform in collide_list:
		# 	if self.delta_x > 0: # dir = "R"
		# 		self.rect.right = platform.rect.left
		# 	elif self.delta_x < 0: # dir = "L"
		# 		self.rect.left = platform.rect.right
		# self.delta_x = 0
		
	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
				
		return ret
