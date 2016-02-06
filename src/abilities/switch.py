import pygame
from ability import Ability

# Switch characters
class Switch(Ability):

	def __init__(self):
		Ability.__init__(self, "switch", pygame.K_f)

	def cast(self, c):
		# Revert if switching to biggie
		if pygame.K_r in c.AI.abilities and c.AI.locked == True:
			c.AI.abilities[pygame.K_r].cast(c)

		# set change to 0 otherwise you get weird behaviour when
		# moving and switching
		c.player.delta_x, c.AI.delta_x = c.AI.delta_x, c.player.delta_x
		c.player, c.AI = c.AI, c.player
		#set both player and AI convo to false to prevent a conversation from starting
		c.player.convo = False;
		c.AI.convo = False;
		c.ACTIVE = c.player
