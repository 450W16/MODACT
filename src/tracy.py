import pygame
from player import Player

class Tracy(Player):
	
	def __init__(self):
		Player.__init__(self)
		
	def jump(self):
		print "tracy jump"
