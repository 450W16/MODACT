import pygame
from os import path
from player import Player
from abilities.climb import *
from directions import Directions
from spritesheet import SpriteSheet
from utils import *

# Default abilities: Climbup, Climbdown
class Tracy(Player):
	
	def __init__(self, x, y):
		Player.__init__(self, x, y)
		
		# initialize lists for walking sprites
		ss = SpriteSheet(path.join(get_art_dir(), 'Tracy', 'Tracy_spritesheet.png'), 8)
		self.sprites_walk_left = ss.get_sprites(size=(32, 64))
		self.sprites_walk_right = [pygame.transform.flip(s, True, False) for s in self.sprites_walk_left]
		
		self.image = self.sprites_walk_right[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		climbUp = ClimbUp()
		self.abilities[climbUp.getKey()] = climbUp
		climbDown = ClimbDown()
		self.abilities[climbDown.getKey()] = climbDown
		
	def move_left(self):
		super(Tracy, self).move_left()

	def move_right(self):
		super(Tracy, self).move_right()
		
	def jump(self):

		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		if len(platform_collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.delta_y = -14

	def stop_y(self, biggieRect):
		self.delta_y = 0
		if self.rect.bottom <= biggieRect.top:
			self.grav = True
			self.horiM = True
			self.col = True
			
	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
			
		# Check for movement
		if not self.is_moving():
			ret = [ret[0]]
		elif self.delta_y != 0:
			ret = [ret[2]]
				
		return ret
