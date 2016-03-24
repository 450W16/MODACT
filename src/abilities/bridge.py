import pygame
from ability import Ability
from characters.directions import Directions
from characters.transformed import Transformed
from characters.directions import Directions

# Transform into a bridge.
class Bridge(Ability):

	def __init__(self):
		Ability.__init__(self, "bridge", pygame.K_b)

	def cast(self, c):
		playerRect = c.player.getRect()
		pl = c.lvl_current.platform_list

		# Check to see if mob will fall off
		# Find platform mob is standing on
		p_cand = None
		# If right, check right of rectangle against platforms
		if c.player.heading == Directions.Right:
			for platform in pl:
				if platform.rect.left < playerRect.right \
				and platform.rect.right >= playerRect.right \
				and playerRect.bottom == platform.rect.top:
					p_cand = platform
					# min_dist = self.rect.bottom - platform.rect.top
		else: # dir = "L" check left of rectangle against platforms
			for platform in pl:
				if platform.rect.right > playerRect.left \
				and platform.rect.left <= playerRect.left \
				and playerRect.bottom == platform.rect.top:
					p_cand = platform

		# Error: falling
		if p_cand == None:
			print "No valid platforms"
			return

		print str(p_cand.rect.x) + " " + str(p_cand.rect.y)
		p_found = False
		if c.player.heading == Directions.Right:
			for platform in pl:
				if platform.rect.left == p_cand.rect.right and platform.rect.top == p_cand.rect.top:
					print "PROBLEM PLATFORM " + str(platform.rect.x) + " " + str(platform.rect.y)
					p_found = True
					break
		else: # dir = "L"
			for platform in pl:
				if platform.rect.right == p_cand.rect.left and platform.rect.top == p_cand.rect.top:
					p_found = True
					break

		if not p_found:
			p_candidates = []
			if c.player.heading == Directions.Right:
				for platform in pl:
					if platform.rect.top == p_cand.rect.top and platform.rect.x > p_cand.rect.x:
						p_candidates.append(platform)
				
				if len(p_candidates) == 0:
					print "Error: Problem!"
					return
				else:
					#find closest wrt x value
					target = p_candidates[0]
					for platform in p_candidates[1:]:
						if platform.rect.x < target.rect.x and platform != p_cand:
							target = platform

				deltaX = abs(p_cand.rect.right - target.rect.left)
				c.player.image = pygame.transform.scale(c.player.image, (deltaX, playerRect.height))
				c.player.rect = pygame.Rect(p_cand.rect.right, target.rect.top, deltaX, playerRect.height)

			elif c.player.heading == Directions.Left:
				for platform in pl:
					if platform.rect.top == p_cand.rect.top and platform.rect.x < p_cand.rect.x:
						p_candidates.append(platform)
				if len(p_candidates) == 0:
					print "Error: problem"
					return
				else:
					#find closest wrt x value
					target = p_candidates[0]
					for platform in p_candidates[1:]:
						if platform.rect.x > target.rect.x and platform != p_cand:
							target = platform
				
				deltaX = abs(p_cand.rect.left - target.rect.right)
				c.player.image = pygame.transform.scale(c.player.image, (deltaX, playerRect.height))
				c.player.rect = pygame.Rect(p_cand.rect.right, target.rect.top, deltaX, playerRect.height)


			c.player.locked = True
			c.player.status = Transformed.Bridge
			c.lvl_current.platform_list.add(c.player)
			c.player.abilities[pygame.K_f].cast(c)
