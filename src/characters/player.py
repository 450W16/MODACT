# player class
import pygame
from abilities.switch import *
from utils import *
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

	def update(self):
		if not self.locked:
			# update movements, gravity, animation, etc.
			if self.grav:
				self.gravity()

			if self.horiM:
				self.rect.x += self.delta_x
				if self.col:
					# collision detection in x
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

			if self.col:
				#detect trigger collision (conversation), set to True to remove event block
				trigger_collide = pygame.sprite.spritecollide(self,
						self.level.trigger_list, True)
				if len(trigger_collide) > 0:
					#start the conversation
					self.convo = True

		
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
		self.heading = Directions.Left

	def move_right(self):
		self.delta_x = 5
		self.heading = Directions.Right

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