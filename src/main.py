#!/bin/python
import pygame
import sys
import ast
import os
import inspect
import pickle
from utils import *
from levels.tutorial_level import Tutorial_level
from levels.level1 import Level1_level
from levels.level2 import Level2_level
from levels.menu_level import Menu_level
from characters.tracy import Tracy
from characters.biggie import Biggie
from levels.platforms import Platform
from camera import Camera

class Control(object):

	def __init__(self, screen):

		# instanciate players and their size
		# self.player = Tracy(100, SCREEN_HEIGHT/2)
		# self.AI = Biggie(0, SCREEN_HEIGHT/2)
		self.player = Tracy(0, SCREEN_HEIGHT - 120)
		self.AI = Biggie(100, SCREEN_HEIGHT - 150)


		# screen
		self.screen = screen

		# create sprite grouping for active sprites
		self.active_sprites = pygame.sprite.Group()
		self.active_sprites.add(self.player)
		self.active_sprites.add(self.AI)

		# which is active
		self.ACTIVE = self.player

		# create level and list of levels
		self.lvl_list = [
							Menu_level(self.player, self.AI),
							Tutorial_level(self.player, self.AI),
							Level1_level(self.player, self.AI),
							Level2_level(self.player, self.AI)
						]
		self.lvl_num = 2
		self.lvl_current = self.lvl_list[self.lvl_num]
		self.player.level = self.lvl_current
		self.AI.level = self.lvl_current

		# some initialization for game loop
		self.done = False
		self.clock=pygame.time.Clock()

		# instantiate camera
		self.camera = Camera()

		self.camera.updateCam(0, 0, self.lvl_current.level_width, self.lvl_current.level_height)

		#conversation variables
		#will change this variable once we refactor, essentially tells main to parse the text file
		self.convoNum = 1
		#dialogue line #
		self.dialogue = 0

	def save(self):
		
		with open('save/save.txt', 'w') as f:
			pickle.dump([self.lvl_num, self.player.abilities, self.AI.abilities], f, protocol=pickle.HIGHEST_PROTOCOL)

	def load(self):
		if os.path.exists('save/save.txt'):
			with open('save/save.txt', 'r') as f:
				
				self.lvl_num, self.player.abilities, self.AI.abilities = pickle.load(f)
				# read in level
				self.lvl_current = self.lvl_list[self.lvl_num]
				#self.camera.updateCam(0, 0, self.lvl_current.level_width, self.lvl_current.level_height)
				self.player.level = self.lvl_current
				self.AI.level = self.lvl_current
				
				# reset player position
				self.player.rect.x = self.lvl_current.Px
				self.player.rect.y = self.lvl_current.Py
				self.AI.rect.x = self.lvl_current.Ax
				self.AI.rect.y = self.lvl_current.Ay
			
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
					if not self.player.convo:
						self.player.jump()
				if event.key == pygame.K_RETURN:
					#if conversation has begun, only return key can progress
					if self.player.convo == True:
						self.dialogue += 1
				else:
					if not self.player.convo:
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


		# follow
		if self.player.delta_x > 0 and self.AI.rect.x < self.player.rect.x - FOLLOW_DIST and not self.AI.locked:
			self.AI.move_right()

		elif self.player.delta_x < 0 and self.AI.rect.x > self.player.rect.right + FOLLOW_DIST and not self.AI.locked:
			self.AI.move_left()

		else:
			self.AI.stop()


		# update level
		self.lvl_current.update(self)

		# check if we've moved onto the next area

		if self.player.rect.right > self.lvl_current.level_width and self.lvl_num < len(self.lvl_list)-1:

			self.lvl_num += 1
			self.save()
			self.lvl_current = self.lvl_list[self.lvl_num]
			self.player.level = self.lvl_current
			self.AI.level = self.lvl_current
			self.player.rect.x = self.lvl_current.Px
			self.player.rect.y = self.lvl_current.Py
			self.AI.rect.x = self.lvl_current.Ax
			self.AI.rect.y = self.lvl_current.Ay

			self.camera.updateCam(0, 0, self.lvl_current.level_width, self.lvl_current.level_height)

		# go to previous area
		elif self.player.rect.left < 0 and self.lvl_num > 0:

			self.lvl_num -= 1
			self.lvl_current = self.lvl_list[self.lvl_num]
			self.player.level = self.lvl_current
			self.AI.level = self.lvl_current

			self.player.rect.y = self.lvl_current.ground_level
			self.AI.rect.y = self.lvl_current.ground_level
			self.player.rect.x = self.lvl_current.level_width-200
			self.AI.rect.x = self.lvl_current.level_width-200

			self.camera.updateCam(self.lvl_current.level_width-SCREEN_WIDTH, self.lvl_current.ground_level, self.lvl_current.level_width, self.lvl_current.level_height)

		elif self.player.rect.left < 0 and self.lvl_num == 0:
			self.player.rect.x = 1
			self.AI.rect.x = 1

	def draw(self):
		self.screen.fill((0,0,0))
		# draw
		self.lvl_current.draw(self.screen, self.camera)

		# draw players
		self.player.image = pygame.transform.scale(self.player.image, self.player.rect.size)
		self.AI.image = pygame.transform.scale(self.AI.image, self.AI.rect.size)
		self.screen.blit(self.AI.image, self.camera.applyCam(self.AI))
		self.screen.blit(self.player.image, self.camera.applyCam(self.player))

		#draw rect at player
		# font = pygame.font.Font(None, 36)
		# label = font.render('TEST TEXT', 1, (0, 255, 0), )
		# self.screen.blit(label, (self.player.rect.left, self.player.rect.bottom))


	def initiateConvo(self):
		#initialize the conversation
		#put each line into the list of 'dialogue'
		if self.player.convo:
			dialogue = []
			if self.convoNum == 1:
				with open(path.join(get_src_dir(), 'tutorial_conversation.txt'), "r") as f:
					dialogue = [x.strip('\n') for x in f.readlines()]

		#lock the player and AI
		self.player.locked = True
		self.AI.locked = True

		# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
		font = pygame.font.Font(None, 48)

		#show the dialogue in a loop until the dialogue is empty
		if dialogue[self.dialogue] != '':
			pygame.draw.rect(self.screen, (0,0,0), (0,0,1000,100))
			label = font.render('Press enter to continue', 1, (255, 255, 255), )
			self.screen.blit(label, (SCREEN_WIDTH/2- 200,0))
			font = pygame.font.Font(None, 26)
			if self.dialogue % 2 != 0:
				# render text for Tracy
				tracyText = font.render(dialogue[self.dialogue], 1, (255, 0, 255), )
				#if the player is currently Tracy, put the dialogue there, otherwise on the other sprite
				if isinstance(self.player,Tracy):
					self.screen.blit(tracyText, (0, 50))
				else:
					self.screen.blit(tracyText, (0, 50))
			else:
				#render text for Biggie
				biggieText = font.render(dialogue[self.dialogue], 1, (0, 0, 255), )
				#if the player is currently Biggie, put the dialogue there, otherwise on the other sprite
				if isinstance(self.player,Biggie):
					self.screen.blit(biggieText, (0, 50))
				else:
					self.screen.blit(biggieText, (0, 50))
		else:
			#unfreeze player and AI, end the conversation with player.convo = False, add one to the dialogue
			# to move to the next conversation line
			self.player.locked = False
			self.AI.locked = False
			self.player.convo = False
			self.dialogue += 1


	def main_loop(self):
		while not self.done:
			
			# input, update, draw
			self.processEvents()
			self.update()
			self.draw()
			#initialize conversation
			if self.player.convo == True:
				self.player.convo = False
				#self.initiateConvo()
			
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
