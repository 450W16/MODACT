import pygame
from moving_platformsUD import MplatformUD
from vine_trigger import VineTrigger
from utils import *

class Vine(MplatformUD):
	
	def __init__(self, x, y, width=28, height=128):
		super(MplatformUD, self).__init__(self, x, y, width, height)
		vine_sprite = pygame.image.load(path.join(get_art_dir(), "Vine.png"))
		self.image = vine_sprite
		self.set_vert_move_amount(5)
		self.vinetrigger = None
		
	def update(self, c):
		if self.vinetrigger is None:
			self.vinetrigger = next((t for t in c.lvl_current.vinetrigger_list if isinstance(t, VineTrigger)), None)
		else:
			# Move vine only if vine trigger is activated
			if self.vinetrigger.activated:
				# Check if the platform hits top boundary
				if self.rect.top <= self.boundary_top:
					pass
				else:
					# Move up
					self.rect.y -= self.change_y
			else:
				# Check if the platform hits bottom boundary
				if self.rect.bottom >= self.boundary_bottom:
					pass
				else:
					# Move down
					self.rect.y += self.change_y
				
		# Check and see if we hit the player
		hit = pygame.sprite.collide_rect(self, c.player)
		if hit:
			# Reset player position based on top/bottom of platform
			if self.change_y < 0:
				c.player.rect.bottom = self.rect.top
			else:
				c.player.rect.top = self.rect.bottom	
