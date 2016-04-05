import pygame
from moving_platforms import MovingPlatform
from utils import *

class MplatformLR(MovingPlatform):

	def __init__(self, player, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):
		super(MplatformLR, self).__init__(player, x, y)
		rock_topend = pygame.image.load(path.join(get_art_dir(), "rock7.png"))
		self.image = rock_topend

	def update(self):
		
		# Move left/right
		self.rect.x += self.change_x

		# Check and see if we hit the player
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# Reset player position based on left/right of platform
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				self.player.rect.left = self.rect.right
 
 		# Check if the platform hits boundaries and reverses direction
 		if self.rect.right > self.boundary_right or self.rect.left < self.boundary_left:
 			self.change_x *= -1
