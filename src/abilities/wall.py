import pygame
from ability import Ability
from characters.transformed import *

class Wall(Ability):

	def __init__(self):
		Ability.__init__(self, "wall", pygame.K_w)

	def cast(self, c):
		if c.player.wallUnlocked:
			playerRect = c.player.rect
			aiRect = c.AI.rect

			left = max(0, aiRect.left - 100)
			right = min(c.lvl_current.level_width, aiRect.right + 100)

			wallHeight = 50
			#c.player.image = pygame.transform.scale(c.player.image, (playerRect.width, wallHeight))
			c.player.image = c.player.sprites_wall[0]
			c.player.rect = pygame.Rect(left, aiRect.top - 75, right-left, wallHeight)
			
			c.player.locked = True
			c.player.status = Transformed.Wall
			c.lvl_current.special_platforms.add(c.player)
			c.player.abilities[pygame.K_f].cast(c)
