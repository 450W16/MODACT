import pygame
from triggers import Trigger
from utils import *

class VineTrigger(Trigger):

	def __init__(self, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):
		super(VineTrigger, self).__init__(x, y, width, height)
		self.activated = False

	def update(self, c):
		hit = pygame.sprite.collide_rect(self, c.player)
		if hit:
			self.activated = True
		else:
			self.activated = False
