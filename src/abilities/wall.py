import pygame
from ability import Ability
from characters.transformed import *

class Wall(Ability):

	def __init__(self):
		Ability.__init__(self, "wall", pygame.K_w)

	def cast(self, c):
		playerRect = c.player.rect

		wallHeight = playerRect.height + 100

		c.player.image = pygame.transform.scale(c.player.image, (playerRect.width, wallHeight))
		c.player.rect = pygame.Rect(playerRect.left, playerRect.top-100, playerRect.width, wallHeight)
		c.player.locked = True
		c.player.status = Transformed.Wall
		c.lvl_current.platform_list.add(c.player)
		c.player.abilities[pygame.K_f].cast(c)