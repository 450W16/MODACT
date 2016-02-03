#!/bin/python
import pygame
import sys
import ast
import os
from utils import *
from levels.tutorial_level import Tutorial_level
from characters.tracy import Tracy
from characters.biggie import Biggie
from levels.platforms import Platform
from camera import Camera

class Control(object):

	def __init__(self, screen):
		# instanciate players and their size
		# self.player = Tracy(100, SCREEN_HEIGHT/2)
		# self.AI = Biggie(0, SCREEN_HEIGHT/2)
		self.player = Tracy(1200, SCREEN_HEIGHT/4)
		self.AI = Biggie(1250, SCREEN_HEIGHT/4)

		# screen
		self.screen = screen

		# create sprite grouping for active sprites
		self.active_sprites = pygame.sprite.Group()
		self.active_sprites.add(self.player)
		self.active_sprites.add(self.AI)

		# which is active
		self.ACTIVE = self.player

		# create level and list of levels
		self.lvl_list = [Tutorial_level(self.player, self.AI)]
		self.lvl_num = 0
		self.lvl_current = self.lvl_list[self.lvl_num]
		self.player.level = self.lvl_current
		self.AI.level = self.lvl_current

		# some initialization for game loop
		self.done = False
		self.clock=pygame.time.Clock()

		# instantiate camera
		self.camera = Camera()

	def save(self):
		with open('save/save.txt', 'w') as f:
			saveStr = str(lvl_no) + ' ' + str(self.player.abilities) + ' ' + str(self.player.abilities)
			f.write(saveStr)

	def load(self):
		if os.path.exists('save/save.txt'):
			with open('save/save.txt', 'r') as f:

				text = f.read()

				if text != '':
					text = text.split(' ')
					text[-1] = text[-1].rstrip('\n')
		
					# read in level
					self.lvl_no = text[0]
					self.current_lvl = self.lvl_list[self.lvl_num]
					self.player.level = self.lvl_current
					self.AI.level = self.lvl_current
					if len(text) > 1:
						# read in abilities
						self.player.abilities = ast.literal_eval(text[1])
						self.AI.abilities = ast.literal_eval(text[2])

		# reset player position
		self.player.rect.x = 50
		self.AI.rect.x = 0	
			
	def processEvents(self):
		# loop events
		for event in pygame.event.get()	:
			if event.type == pygame.QUIT:
				self.done = True
			# key pressed 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.player.move_left()
				if event.key == pygame.K_RIGHT:
					self.player.move_right()
				if event.key == pygame.K_SPACE:
					self.player.jump()
				else:
					# check for ability key
					k = self.player.checkAbility(event.key)
					if k is not None:
						k.cast(self)
			# key released
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and self.player.delta_x < 0:
					self.player.stop()
				if event.key == pygame.K_RIGHT and self.player.delta_x > 0:
					self.player.stop()
				if event.key == pygame.K_UP and self.player.delta_y < 0:
					if isinstance(self.player, Tracy):
						self.player.stop_y(self.AI.rect)
					else:
						self.player.stop()
				if event.key == pygame.K_DOWN and self.player.delta_y > 0:
					if isinstance(self.player, Tracy):
						self.player.stop_y(self.AI.rect)
					else:
						self.player.stop()
			

	def update(self):
		# update camera
		self.camera.update(self.player)			

		#update player
		self.active_sprites.update()
		if self.player.dead:
			self.load()
			self.player.dead = False
			
		# update level
		self.lvl_current.update()

		# check if we've moved onto the next area
		if self.player.rect.right > LEVEL_WIDTH and self.lvl_num < len(self.lvl_list)-1:
			# save checkpoint
			self.save()
			self.player.rect.x = 50
			self.AI.rect.x = 0
			self.lvl_num += 1
			self.lvl_current = self.lvl_list[self.lvl_num]
			self.player.level = self.lvl_current
			self.AI.level = self.lvl_current

		# go to previous area
		elif self.player.rect.left < 0 and self.lvl_num > 0:
			self.player.rect.x = LEVEL_WIDTH-100
			self.player.rect.x = LEVEL_WIDTH
			self.lvl_num -= 1
			self.lvl_current = self.lvl_list[lvl_num]
			self.player.level = self.lvl_current
			self.AI.level = self.lvl_current

	def draw(self):
		# draw
		self.lvl_current.draw(self.screen, self.camera)

		# draw players
		self.screen.blit(self.AI.image, self.camera.applyCam(self.AI))
		self.screen.blit(self.player.image, self.camera.applyCam(self.player))

	def main_loop(self):
		while not self.done:
			
			# input, update, draw
			self.processEvents()
			self.update()
			self.draw()
			
			#FPS		
			self.clock.tick(60)
			
			#refresh screen
			pygame.display.flip()

def main():

	# initialize pygame
	pygame.init()

	# initialize screen
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("This is a game... or is it")

	Control(screen).main_loop()
	pygame.quit()

if __name__ == "__main__":
	main()
