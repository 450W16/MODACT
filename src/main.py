#!/bin/python
import pygame
import sys
import ast
import os
import inspect
from utils import *
from levels.tutorial_level import Tutorial_level
from levels.level1 import Level1_level
from characters.tracy import Tracy
from characters.biggie import Biggie
from levels.platforms import Platform
from camera import Camera

class Control(object):

	def __init__(self, screen):
		# instanciate players and their position
		self.player = Tracy(0, SCREEN_HEIGHT - 224)
		self.AI = Biggie(100, SCREEN_HEIGHT - 224)

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
							Tutorial_level(self.player, self.AI),
							Level1_level(self.player, self.AI)
						]	
		self.lvl_num = 0
		self.lvl_current = self.lvl_list[self.lvl_num]
		self.player.level = self.lvl_current
		self.AI.level = self.lvl_current

		# some initialization for game loop
		self.done = False
		self.clock=pygame.time.Clock()

		# instantiate camera
		self.camera = Camera()

		#conversation variables
		#will change this variable once we refactor, essentially tells main to parse the text file
		self.convoNum = 1 
		#dialogue line #
		self.dialogue = 0



	def save(self):
		pass
		#with open('save/save.txt', 'w') as f:
		#	saveStr = str(self.lvl_num) + ' ' + str(self.player.abilities) + ' ' + str(self.AI.abilities)
		#	f.write(saveStr)

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
				if event.key == pygame.K_RETURN:
					#if conversation has begun, only return key can progress
					if self.player.convo == True:
						self.dialogue += 1
				else:
					# check for ability key
					k = self.player.checkAbility(event.key)
					if k is not None:
						k.cast(self)
			# key released
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and self.player.delta_x < 0:
					self.player.stop()
					self.AI.stop()
				if event.key == pygame.K_RIGHT and self.player.delta_x > 0:
					self.player.stop()
					self.AI.stop()
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
			
		# update level
		self.lvl_current.update(self)

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
			self.lvl_current = self.lvl_list[self.lvl_num]
			self.player.level = self.lvl_current
			self.AI.level = self.lvl_current
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
		#print(str(self.AI.rect.height))

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
			label = font.render('Press enter to continue', 1, (255, 255, 255), )
			self.screen.blit(label, (0,0))
			font = pygame.font.Font(None, 24)
			if self.dialogue % 2 != 0:
				# render text for Tracy
				tracyText = font.render(dialogue[self.dialogue], 1, (255, 0, 255), )
				#if the player is currently Tracy, put the dialogue there, otherwise on the other sprite
				if isinstance(self.player,Tracy):
					self.screen.blit(tracyText, (self.player.rect.left, self.player.rect.top - 100))	
				else:
					self.screen.blit(tracyText, (self.AI.rect.left, self.AI.rect.top - 100))
			else:
				#render text
				biggieText = font.render(dialogue[self.dialogue], 1, (0, 0, 255), )
				#if the player is currently Biggie, put the dialogue there, otherwise on the other sprite
				if isinstance(self.player,Biggie):
					self.screen.blit(biggieText, (self.player.rect.left, self.player.rect.top - 100))	
				else:
					self.screen.blit(biggieText, (self.AI.rect.left, self.AI.rect.top - 100))
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
				self.initiateConvo()
			
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
