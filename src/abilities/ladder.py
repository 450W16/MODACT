import pygame
from ability import Ability
from characters.transformed import Transformed

# TODO: Handle stop events without keypress
# Transform into a ladder.
class Ladder(Ability):

	def __init__(self):
		Ability.__init__(self, "ladder", pygame.K_l)

	def cast(self, c):
		playerRect = c.player.getRect()
		platformList = c.lvl_current.platform_list
		p_candidates = []
		# Get all platforms above character
		for platform in platformList:
			# y axis is top to bottom
			if platform.rect.center[0] > playerRect.left and platform.rect.center[0] < playerRect.right and platform.rect.y < playerRect.top:
				p_candidates.append(platform)
		# No targets
		if len(p_candidates) == 0:
			return
		else:
			# Find the highest one (lowest y)
			pf = p_candidates[0]
			for platform in p_candidates[1:]:
				if platform.rect.y < pf.rect.y:
					pf = platform

		# Modify rect/img, lock character, and then switch
		deltaY = abs(pf.rect.top - playerRect.bottom)
		#c.player.image = pygame.transform.scale(c.player.image, (playerRect.width, deltaY))
		c.player.image = c.player.sprites_ladder[0]
		c.player.rect = pygame.Rect(playerRect.left, pf.rect.top, playerRect.width, deltaY)
		c.player.locked = True
		c.player.status = Transformed.Ladder
		c.player.abilities[pygame.K_f].cast(c)
