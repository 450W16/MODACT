# Modified from stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame
import pygame
from utils import *

class Camera(object):
	
	def __init__(self):
		self.state = pygame.Rect(0,0, LEVEL_WIDTH, LEVEL_HEIGHT)

	def applyCam(self, target):
		try:
			t = target.rect.move(self.state.topleft)
		except:
			try:
				t = target.get_rect().move(self.state.topleft)
			except:
				t = target.move(self.state.topleft)
		return t
	
	def update(self, target):
		self.state = self.cam_func(target.rect)

	def cam_func(self, target):
		l, t, _, _ = target
		_, _, w, h = self.state
		l, t, _, _ = -l + int(SCREEN_WIDTH/2) , -t + int(SCREEN_HEIGHT/2), w, h

		l = min(0,l)
		l = max(-(self.state.width-SCREEN_WIDTH), l)
		t = max(-(self.state.height-SCREEN_HEIGHT), t)
		t = min(0,t)
		
		return pygame.Rect(l, t, w, h)
