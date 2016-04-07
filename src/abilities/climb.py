import pygame
from ability import Ability
from characters.transformed import Transformed

class ClimbUp(Ability):

	def __init__(self):
		Ability.__init__(self, "climbUp", pygame.K_UP)

	def cast(self, c):
		biggieRect = c.AI.getRect()
		tracyRect = c.player.getRect()
		c.climbing = 1
	
		if biggieRect.colliderect(tracyRect) and c.AI.status == Transformed.Ladder:
			
			if tracyRect.bottom <= biggieRect.top:
				c.climbing = 0
				c.player.delta_y = 0
				c.player.grav = True 
				c.player.horiM = True
				c.player.col = True
				c.player.climbing = False
			else:
				c.player.delta_y = -2
				c.player.rect.left = biggieRect.left + 20
				c.player.grav = False
				c.player.horiM = False
				c.player.col = False
				c.player.climbing = True
		else:
			c.climbing = 0
			c.player.delta_y = 0
			c.player.grav = True 
			c.player.horiM = True
			c.player.col = True
			c.player.climbing = False

class ClimbDown(Ability):
	def __init__(self):
		Ability.__init__(self, "climbDown", pygame.K_DOWN)

	def cast(self, c):
		biggieRect = c.AI.getRect()
		tracyRect = c.player.getRect()
		c.climbing = 2

		if (biggieRect.colliderect(tracyRect) or biggieRect.collidepoint(tracyRect.center[0],tracyRect.bottom)) and c.AI.status == Transformed.Ladder:
			if tracyRect.bottom >= biggieRect.bottom:
				c.climbing = 0
				c.player.delta_y = 0
				c.player.grav = True
				c.player.horiM = True
				c.player.col = True
				c.player.climbing = False
			else:
				c.player.delta_y = 2
				c.player.rect.left = biggieRect.left + 20
				c.player.grav = False
				c.player.horiM = False
				if tracyRect.bottom > biggieRect.bottom - 50:
					c.player.col = True
				else:
					c.player.col = False
				c.player.climbing = True
		else:
			c.player.climbing = False
