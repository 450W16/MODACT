import pygame
from player import Player
from abilities.bridge import *
from abilities.ladder import Ladder
from abilities.wall import *
from spritesheet import SpriteSheet
from utils import *

# Default abilities: Ladder, Bridge, Reverts
class Biggie(Player):
	
	def __init__(self, x, y):
		Player.__init__(self, x, y)

		# initialize list for walking sprites
		ss = SpriteSheet(path.join(get_art_dir(), 'Biggie', 'Biggie_spritesheet.png'), 10)
		self.sprites_walk_right = ss.get_sprites(size=(96, 96))
		self.sprites_walk_left = [pygame.transform.flip(s, True, False) for s in self.sprites_walk_right]
		ss = SpriteSheet(path.join(get_art_dir(), 'Biggie', 'Bridge.png'), 8)
		self.sprites_bridge = ss.get_sprites(size=(256, 32))
		ss = SpriteSheet(path.join(get_art_dir(), 'Biggie', 'Ladder.png'), 8)
		self.sprites_ladder = ss.get_sprites(size=(32, 256))
		ss = SpriteSheet(path.join(get_art_dir(), 'Biggie', 'Umbrella.png'), 8)
		self.sprites_wall = ss.get_sprites(size=(200, 83))
		
		self.heading = Directions.Left
		self.image = self.sprites_walk_left[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rect.width = BIGGIE_WIDTH
		self.rect.height = BIGGIE_HEIGHT
		self.image = pygame.transform.scale(self.image, self.rect.size)
		ladder = Ladder()
		self.abilities[ladder.getKey()] = ladder
		bridge = Bridge()
		self.abilities[bridge.getKey()] = bridge
		wall = Wall()
		self.abilities[wall.getKey()] = wall
		self.status = Transformed.Default

		self.wallUnlocked = False
		
	def jump(self):

		#check if we're on the ground
		self.rect.y += 2
		platform_collisions = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
		#if yes, set trajectory upwards
		# will have to change if we change ground
		if len(platform_collisions) > 0 or self.rect.bottom >= self.level.level_height:
			self.delta_y = -20

		jump_sound = pygame.mixer.Sound("characters/tracy_jump.wav")
		jump_sound.play()

	def get_sprites(self):
		ret = None
		if self.heading == Directions.Left:
			ret = self.sprites_walk_left
		elif self.heading == Directions.Right:
			ret = self.sprites_walk_right
		
		# Check for movement
		if not self.is_moving():
			ret = [ret[9]]
		elif self.delta_y != 0:
			ret = [ret[0]]
			

				
		return ret
		
