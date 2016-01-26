import pygame

class Ability(pygame.sprite.Sprite):

	def __init__(self, name, keybind):

		self.name = name
		self.keybind = keybind

	def cast(self):
		pass

	def getKey(self):
		return self.keybind

	def __str__(self):
		return self.name