import pygame
from ability import Ability

class Switch(Ability):

	def __init__(self):
		Ability.__init__(self, "switch", pygame.K_f)

	def cast(self, c):
		# set change to 0 otherwise you get weird behaviour when
		# moving and switching
		c.player.delta_x, c.AI.delta_x = c.AI.delta_x, c.player.delta_x
		c.player, c.AI = c.AI, c.player
		c.ACTIVE = c.player
