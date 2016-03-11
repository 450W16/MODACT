import pygame

class Enemy(pygame.sprite.Sprite):
		
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface((width, height))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		
		# TODO: maybe move this counter to the future Moveable class.
		# Sprite animation counter
		self.curr_sprite_index = 0
		self.update_counter = 0
		self.frames_per_sprite = 2

	def get_sprites(self):
		raise NotImplementedError("Please implement this method")
		
	def update(self):
		self.update_sprites()
		
	def update_sprites(self):
		if self.get_sprites():
			self.update_counter = (self.update_counter + 1) % self.frames_per_sprite
			if self.update_counter == 0:
				self.curr_sprite_index = (self.curr_sprite_index + 1) % len(self.get_sprites())
				self.image = self.get_sprites()[self.curr_sprite_index]