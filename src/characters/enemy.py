import pygame
from utils import *

class Enemy(pygame.sprite.Sprite):
		
	def __init__(self, width, height, x, y):
		pygame.sprite.Sprite.__init__(self)
		if width <= BLOCK_WIDTH:
			print "WARNING WIDTH MAY CAUSE PROBLEMS"
		self.image = pygame.Surface((width, height))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.delta_y = 0
		self.delta_x = 0
		self.rect.x = x
		self.rect.y = y
		self.aggroRange = 300
		print(str(self.rect.x) + " " + str(self.rect.y))
	
	def checkAggro(self, c, default):
		# Check aggro
		dist =  c.player.rect.x - self.rect.x
		if abs(dist) < self.aggroRange:
			# Close enough, set direction
			if default:
				if dist > 0:
					self.dir = "R"
					self.delta_x += self.speed
				else:
					self.dir = "L"
					self.delta_x -= self.speed

			return True

		return False

	# Basic left right mob update
	def update(self, c):
		print(str(self.rect.x) + " " + str(self.rect.y))
		self.gravity()

		# Check aggro
		if not self.checkAggro(c, True):
			if self.dir == "R":
				self.delta_x += self.speed
			else: # self.dir = "L"
				self.delta_x -= self.speed

		pl = c.lvl_current.platform_list

		# collision detection in y 
		# check first so mob is positioned properly on top of platform
		self.rect.y += self.delta_y
		collide_list = pygame.sprite.spritecollide(self, pl, False)
		for platform in collide_list:
			if self.delta_y > 0:
				self.rect.bottom = platform.rect.top
			elif self.delta_y < 0:
				self.rect.top = platform.rect.bottom
			self.delta_y = 0


		# Check to see if mob will fall off
		# Find platform mob is standing on
		p_cand = None
		# If right, check right of rectangle against platforms
		if self.dir == "R":
			for platform in pl:
				if platform.rect.left < self.rect.right \
				and platform.rect.right >= self.rect.right \
				and self.rect.bottom == platform.rect.top:
					p_cand = platform
					# min_dist = self.rect.bottom - platform.rect.top
		else: # dir = "L" check left of rectangle against platforms
			for platform in pl:
				if platform.rect.right > self.rect.left \
				and platform.rect.left <= self.rect.left \
				and self.rect.bottom == platform.rect.top:
					p_cand = platform

		# Error: falling
		if p_cand == None:
			print "ERROR: FALLING"
			return

		p_found = False
		if self.dir == "R":
			for platform in pl:
				if platform.rect.left == p_cand.rect.right and platform.rect.top == p_cand.rect.top:
					p_found = True
					break
		else: # dir = "L"
			for platform in pl:
				if platform.rect.right == p_cand.rect.left and platform.rect.top == p_cand.rect.top:
					p_found = True
					break

		# Reverse directions if at edge
		if not p_found:
			if self.dir == 'R':
				if self.rect.right >= p_cand.rect.right:
					self.dir = 'L'
					self.delta_x = 0
			else:
				if self.rect.left <= p_cand.rect.left:
					self.dir = 'R'
					self.delta_x = 0


		# collision detection in x
		# If collide with wall, reverse direction
		self.rect.x += self.delta_x
		collide_list = pygame.sprite.spritecollide(self, pl, False)
		for platform in collide_list:
			if self.delta_x > 0: # dir = "R"
				self.rect.right = platform.rect.left
				self.dir = "L"
			elif self.delta_x < 0: # dir = "L"
				self.rect.left = platform.rect.right
				self.dir = "R"
		self.delta_x = 0


	def gravity(self):
		if self.delta_y == 0:
			self.delta_y = 1
		else:
			self.delta_y += 1 

		# check if we're on the ground
		if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.delta_y >= 0:
			self.delta_y = 0
			self.rect.y = SCREEN_HEIGHT - self.rect.height
