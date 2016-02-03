import pygame
from ability import Ability
from characters.directions import Directions
from characters.transformed import Transformed

# TODO: Implement gap detection
# Transform into a bridge.
class Bridge(Ability):

	def __init__(self):
		Ability.__init__(self, "bridge", pygame.K_b)

	def cast(self, c):
		playerRect = c.player.getRect()
		platformList = c.lvl_current.platform_list
		p_candidates = []
		# Get all platforms below character
		for platform in platformList:
			# y axis is top to bottom
			if platform.rect.center[0] > playerRect.left and platform.rect.center[0] < playerRect.right and platform.rect.y > playerRect.top:
				p_candidates.append(platform)
		# No targets
		if len(p_candidates) == 0:
			print "PROBLEM?"
			return
		else:
			# Find the closest one (also the highest)
			pf = p_candidates[0]
			for platform in p_candidates[1:]:
				if platform.rect.y < pf.rect.y:
					pf = platform

		p_candidates = []
		# Find platforms on the same y as pf
		if c.player.heading == Directions.Right:
			# Candidates to the right of base
			for platform in platformList:
				if platform.rect.center[1] > pf.rect.top and platform.rect.center[1] < pf.rect.bottom:
					if platform.rect.x > pf.rect.x:
						p_candidates.append(platform)


			if len(p_candidates) == 0:
				print "PROBLEM!"
				return
			else:
				# Find closest wrt x value
				target = p_candidates[0]
				for platform in p_candidates[1:]:
					if platform.rect.x < target.rect.x:
						target = platform

			# Modify rect/img, lock character, and then switch
			deltaX = abs(pf.rect.right - target.rect.left)
			c.player.image = pygame.transform.scale(c.player.image, (deltaX, playerRect.height))
			c.player.rect = pygame.Rect(pf.rect.right, pf.rect.top, deltaX, playerRect.height)

		# Reverse some values for creating bridge in other direction
		elif c.player.heading == Directions.Left:
			# Candidates to the left of base
			for platform in platformList:
				if platform.rect.center[1] > pf.rect.top and platform.rect.center[1] < pf.rect.bottom:
					if platform.rect.x < pf.rect.x:
						p_candidates.append(platform)

			if len(p_candidates) == 0:
				print "PROBLEM!"
				return
			else:
				# Find closest wrt x value
				target = p_candidates[0]
				for platform in p_candidates[1:]:
					if platform.rect.x > target.rect.x:
						target = platform

			deltaX = abs(pf.rect.left - target.rect.right)
			c.player.image = pygame.transform.scale(c.player.image, (deltaX, playerRect.height))
			c.player.rect = pygame.Rect(target.rect.right, target.rect.top, deltaX, playerRect.height)

		c.player.locked = True
		c.player.status = Transformed.Bridge
		c.lvl_current.platform_list.add(c.player)
		c.player.abilities[pygame.K_f].cast(c)