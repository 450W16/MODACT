import pygame
from ability import Ability

class Switch(Ability):

	def __init__(self):
		Ability.__init__(self, "switch", pygame.K_f)

	def cast(self):
		def switch(c):
			# set change to 0 otherwise you get weird behaviour when
			# moving and switching
			c.player.delta_x = 0
			c.player, c.AI = c.AI, c.player
			c.ACTIVE = c.player
		return switch