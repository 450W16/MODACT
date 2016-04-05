import pygame
from moving_platformsUD import MplatformUD
from utils import *

class Vine(MplatformUD):
	
	def __init__(self, player, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):
		super(MplatformUD, self).__init__(player, x, y)
		self.set_vert_move_amount(3)
		
	def update(self):
		# TODO: Modify update based on trigger event
		
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
