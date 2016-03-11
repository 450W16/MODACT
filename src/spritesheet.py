import pygame
from utils import *

class SpriteSheet(object):
	"""Sprite sheet handler."""
	
	def __init__(self, filename, num_sprites):
		"""Inits SpriteSheet using the given filename and number of sprites.
		
		Args:
			filename: the filename of the sprite sheet.
			num_sprites: the number of individual sprites in the sprite sheet.
		"""
		self.sprite_sheet = pygame.image.load(filename).convert_alpha()
		self.num_sprites = num_sprites
		
	def get_sprites(self, pos=(0,0), size=(BLOCK_WIDTH, BLOCK_HEIGHT)):
		"""Returns a list containing the images in a sprite sheet
		
		Args:
			pos: the position of the first sprite in the sprite sheet
			size: the (width, height) of each individual sprite
		Returns:
			a list containing the images in a sprite sheet
		"""
		sprites = []
		sprite_pos_x, sprite_pos_y = pos
		sprite_width, sprite_height = size
		sheet_rect = self.sprite_sheet.get_rect()
		n = 0
		for i in range(0, sheet_rect.height, sprite_height):
			for j in range(0, sheet_rect.width, sprite_width):
				self.sprite_sheet.set_clip(pygame.Rect(sprite_pos_x, sprite_pos_y, sprite_width, sprite_height))
				sprite = self.sprite_sheet.subsurface(self.sprite_sheet.get_clip())
				sprites.append(sprite)
				sprite_pos_x += sprite_width
				n += 1
				if n == self.num_sprites:
					return sprites
					
			sprite_pos_y += sprite_height
			sprite_pos_x = 0
			
		return sprites