import pygame
from moving_platforms import MovingPlatform
from utils import *

class MplatformUD(MovingPlatform):
	
	def __init__(self, player, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):
		super(MplatformUD, self).__init__(player, x, y)
		rock_topend = pygame.image.load(path.join(get_art_dir(), "rock7.png"))
		self.image = rock_topend
	
	def update(self):
		
		# Move up/down
		self.rect.y += self.change_y
		
		# Check and see if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# Reset player position based on top/bottom of platform
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				self.player.rect.top = self.rect.bottom
				
		# Check if the platform hits boundaries and reverses direction
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
