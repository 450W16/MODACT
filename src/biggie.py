import pygame
from player import Player

class Biggie(Player):
	
	def __init__(self):
		Player.__init__(self)
		
	def jump(self):
		print "biggie jump"
		#check if we're on the ground
		#if yes, set trajectory upwards
		
		
