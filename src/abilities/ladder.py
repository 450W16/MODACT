import pygame

class Ladder(Ability):

	def __init__(self):
		Ability.__init__(self, "ladder", pygame.K_l)

	def cast(self, c):
		