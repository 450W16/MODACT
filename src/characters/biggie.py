import pygame
from player import Player
from abilities.bridge import *
from abilities.ladder import Ladder
from abilities.revert import Revert
from spritesheet import SpriteSheet
from utils import *

# Default abilities: Ladder, Bridge, Reverts
class Biggie(Player):
	
	def __init__(self, x, y):
		Player.__init__(self, x, y)

		# initialize list for walking sprites
		ss = SpriteSheet(path.join(get_art_dir(), 'Biggie', 'Biggie_spritesheet.png'), 10)
		self.sprites_walk_right = ss.get_sprites()
		self.sprites_walk_left = [pygame.transform.flip(s, True, False) for s in self.sprites_walk_right]
		self.curr_sprite_index = 0
		
		self.image = self.sprites_walk_right[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		ladder = Ladder()
		self.abilities[ladder.getKey()] = ladder
		revert = Revert()
		self.abilities[revert.getKey()] = revert
		bridge = Bridge()
		self.abilities[bridge.getKey()] = bridge
		self.status = Transformed.Default
		
	def jump(self):

		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		# will have to change if we change ground
		if len(platform_collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.delta_y = -20
		
	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
				
		return ret