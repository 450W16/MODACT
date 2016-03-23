import pygame
from moving_platformsUD import MplatformUD
from utils import *

class Vine(MplatformUD):
	
	def __init__(self, player, x, y, width=BLOCK_WIDTH, height=BLOCK_HEIGHT):
		super(MplatformUD, self).__init__(player, x, y)
		self.set_vert_move_amount(3)
	