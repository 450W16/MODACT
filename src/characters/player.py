# player class
import pygame
from abilities.switch import *
from utils import *
from spritesheet import SpriteSheet
from directions import Directions

class Player(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		# change in x and y
		self.delta_x = 0
		self.delta_y = 0

		#players level
		self.level = None

		# player's abilities
		switch = Switch()
		self.abilities = {switch.getKey(): switch}

		# player dead
		self.dead = False

		# Allow collision
		self.col = True
		# Allow gravity
		self.grav = True
		# Allow horizontal movement
		self.horiM = True
		# Allow vertical movement
		self.vertM = True
		# Locked
		self.locked = False
		# Default heading
		self.heading = Directions.Right
		# Conversation?
		self.convo = True
		
		# TODO: maybe move this counter to the future Moveable class.
		# Sprite animation counter
		self.curr_sprite_index = 0
		self.update_counter = 0
		self.frames_per_sprite = 3

	def update(self):
		if not self.locked:
			# update movements, gravity, animation, etc.

			if not self.convo:
				self.update_sprites()

			
				if self.grav:
					self.gravity()

				if self.horiM:
					self.rect.x += self.delta_x
					if self.delta_x > 0:
						self.heading = Directions.Right
					elif self.delta_x < 0:
						self.heading = Directions.Left
					if self.col:
						# collision detection in X 					
						collide_list = pygame.sprite.spritecollide(self, 
								self.level.platform_list, False)
						for platform in collide_list:
							if self.delta_x > 0:
								self.rect.right = platform.rect.left
							elif self.delta_x < 0:
								self.rect.left = platform.rect.right

				if self.vertM:
					self.rect.y += self.delta_y

					if self.col:
						# collision detection in y
						collide_list = pygame.sprite.spritecollide(self, 
								self.level.platform_list, False)
						for platform in collide_list:
							if self.delta_y > 0:
								self.rect.bottom = platform.rect.top
							elif self.delta_y < 0:
								self.rect.top = platform.rect.bottom
							self.delta_y = 0
				
				if self.col:
					# detect enemy collision
					enemy_collide = pygame.sprite.spritecollide(self, 
							self.level.enemy_list, False)
					if len(enemy_collide) > 0:
						self.dead = True
					# collision detection in X 					
					collide_list = pygame.sprite.spritecollide(self, 
							self.level.platform_list, False)
					for platform in collide_list:
						if self.delta_x > 0:
							self.rect.right = platform.rect.left
						elif self.delta_x < 0:
							self.rect.left = platform.rect.right

			if self.vertM:
				self.rect.y += self.delta_y
				if self.col:
					#detect trigger collision (conversation), set to True to remove event block
					trigger_collide = pygame.sprite.spritecollide(self,
							self.level.trigger_list, True)
					if len(trigger_collide) > 0:
						#start the conversation
						self.convo = True

		if self.convo:
			#if in a conversation, allow y movement to fix the stuck in the air bug
			#temporary solution
			self.rect.y += self.delta_y

			if self.col:
				# collision detection in y
				collide_list = pygame.sprite.spritecollide(self, 
						self.level.platform_list, False)
				for platform in collide_list:
					if self.delta_y > 0:
						self.rect.bottom = platform.rect.top
					elif self.delta_y < 0:
						self.rect.top = platform.rect.bottom
					self.delta_y = 0

		
	def gravity(self):
		if self.delta_y == 0:
			self.delta_y = 1
		else:
			self.delta_y += 1 

		# check if we're on the ground
		if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.delta_y >= 0:
			self.delta_y = 0
			self.rect.y = SCREEN_HEIGHT - self.rect.height
	
	def move_left(self):
		self.delta_x = -5
		#self.heading = Directions.Left

	def move_right(self):
		self.delta_x = 5
		#self.heading = Directions.Right

	def jump(self):
		pass

	def stop(self):
		self.delta_x = 0
		self.delta_y = 0

	def getAbilities(self):
		return self.abilities

	def checkAbility(self, key):
		if key in self.abilities:
			return self.abilities[key]
		else:
			return None

	def getRect(self):
		return self.rect
		
	def get_sprites(self):
		raise NotImplementedError("Please implement this method")
		
	def is_moving(self):
		return self.delta_x != 0 or self.delta_y != 0

	def update_sprites(self):
		if self.get_sprites():
			self.update_counter = (self.update_counter + 1) % self.frames_per_sprite
			if self.update_counter == 0:
				self.curr_sprite_index = (self.curr_sprite_index + 1) % len(self.get_sprites())
				self.image = self.get_sprites()[self.curr_sprite_index]