import pygame
from player import Player

class Biggie(Player):
	
	def __init__(self):
		Player.__init__(self)
		
	def jump(self):
		print "biggie jump"
