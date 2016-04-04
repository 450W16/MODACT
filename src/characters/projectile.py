import pygame

class Projectile(pygame.sprite.Sprite):

	def __init__(self, width, height, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width, height))
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		# Sprite animation counter
		self.curr_sprite_index = 0
		self.frame_counter = 0
		self.frames_per_sprite = 4

	def update(self, c):
		self.update_sprites()
		
	def get_sprites(self):
		raise NotImplementedError("Please implement this method")

	def update_sprites(self):
		if self.get_sprites():
			self.frame_counter = (self.frame_counter + 1) % self.frames_per_sprite
			if self.frame_counter == 0:
				self.curr_sprite_index = (self.curr_sprite_index + 1) % len(self.get_sprites())
				self.image = self.get_sprites()[self.curr_sprite_index]
