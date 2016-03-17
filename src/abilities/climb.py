import pygame
from ability import Ability

class ClimbUp(Ability):

	def __init__(self):
		Ability.__init__(self, "climbUp", pygame.K_UP)

	def cast(self, c):
		biggieRect = c.AI.getRect()
		tracyRect = c.player.getRect()
	
		if biggieRect.colliderect(tracyRect) and c.AI.locked == True:
			
			#if tracyRect.bottom <= biggieRect.top:
			#	print("ayy lmao")
			#	c.player.delta_y = 0
			#	c.player.grav = True 
			#	c.player.horiM = True
			#	c.player.col = True
			#else:
			c.player.delta_y = -2
			c.player.rect.left = biggieRect.left + 10
			c.player.grav = False
			c.player.horiM = False
			c.player.col = False

class ClimbDown(Ability):
	def __init__(self):
		Ability.__init__(self, "climbDown", pygame.K_DOWN)

	def cast(self, c):
		biggieRect = c.AI.getRect()
		tracyRect = c.player.getRect()

		print(str(tracyRect.center[0]) + " " + str(biggieRect.center[0]))
		print(str(tracyRect.bottom) + " " + str(biggieRect.top))
		if (biggieRect.colliderect(tracyRect) or biggieRect.collidepoint(tracyRect.center[0],tracyRect.bottom)) and c.AI.locked == True:
			if tracyRect.bottom >= biggieRect.bottom:
				print("hi")
				c.player.delta_y = 0
				c.player.grav = True
				c.player.horiM = True
				c.player.col = True
			else:
				c.player.delta_y = 2
				c.player.rect.left = biggieRect.left + 10
				c.player.grav = False
				c.player.horiM = False
				c.player.col = True
