import pygame

class Bridge(Ability):

	def __init__(self):
		Ability.__init__(self, "bridge", pygame.K_b)

	def cast(self, c):
		pass
