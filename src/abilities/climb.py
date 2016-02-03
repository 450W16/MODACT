import pygame
from ability import Ability

class ClimbUp(Ability):

	def __init__(self):
		Ability.__init__(self, "climbUp", pygame.K_UP)

	def cast(self, c):
		biggieRect = c.AI.getRect()
		tracyRect = c.player.getRect()

		if abs(biggieRect.left - tracyRect.left) < 10 and abs(biggieRect.right - tracyRect.right) < 10 and c.AI.locked == True:
			if tracyRect.bottom <= biggieRect.top:
				c.player.delta_y = 0
				c.player.grav = True
				c.player.horiM = True
				c.player.col = True
			else:
				c.player.delta_y = -2
				c.player.rect.left = biggieRect.left
				c.player.rect.right = biggieRect.right
				c.player.grav = False
				c.player.horiM = False
				c.player.col = False

class ClimbDown(Ability):
	def __init__(self):
		Ability.__init__(self, "climbDown", pygame.K_DOWN)

	def cast(self, c):
		biggieRect = c.AI.getRect()
		tracyRect = c.player.getRect()

		if abs(biggieRect.left - tracyRect.left) < 10 and abs(biggieRect.right - tracyRect.right) < 10 and c.AI.locked == True:
			if tracyRect.bottom >= biggieRect.bottom:
				c.player.delta_y = 0
				c.player.grav = True
				c.player.horiM = True
				c.player.col = True
			else:
				c.player.delta_y = 2
				c.player.rect.left = biggieRect.left
				c.player.rect.right = biggieRect.right
				c.player.grav = False
				c.player.horiM = False
				c.player.col = False
