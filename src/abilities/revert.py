import pygame
from utils import *
from ability import Ability
from characters.transformed import Transformed
from characters.directions import Directions

# Revert is called in switch, it is used to revert Biggie back to his normal size
class Revert(Ability):

	def __init__(self):
		Ability.__init__(self, "revert", pygame.K_r)

	# Revert before switching so Biggie = AI
	# Revert his rec/image and unlock him
	def cast(self, c):
		if c.AI.status == Transformed.Ladder:
			c.AI.image = pygame.transform.scale(c.AI.image, (BIGGIE_WIDTH, BIGGIE_HEIGHT))
			c.AI.rect = pygame.Rect(c.AI.rect.left, c.AI.rect.top - BIGGIE_HEIGHT, BIGGIE_WIDTH, BIGGIE_HEIGHT)
		elif c.AI.status == Transformed.Bridge:
			c.lvl_current.platform_list.remove(c.AI)
			c.AI.image = pygame.transform.scale(c.AI.image, (BIGGIE_WIDTH, BIGGIE_HEIGHT))
			if c.AI.heading == Directions.Left:
				c.AI.rect = pygame.Rect(c.AI.rect.left - BIGGIE_WIDTH, c.AI.rect.top - BIGGIE_HEIGHT, BIGGIE_WIDTH, BIGGIE_HEIGHT)
			elif c.AI.heading == Directions.Right:
				c.AI.rect = pygame.Rect(c.AI.rect.right, c.AI.rect.top - BIGGIE_HEIGHT, BIGGIE_WIDTH, BIGGIE_HEIGHT)
			else:
				print "PROBLEM#"

		c.AI.locked = False
		c.AI.status = Transformed.Default
