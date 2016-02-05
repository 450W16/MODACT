# A file for non-class related utility and constants
from os import path

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
PLAYER_HEALTH = 10
BIGGIE_WIDTH, BIGGIE_HEIGHT = 40, 60
TRACY_WIDTH, TRACY_HEIGHT = 40, 30
ACTIVE = None
LEVEL_WIDTH,LEVEL_HEIGHT = 2100, 3000
BLOCK_WIDTH = BLOCK_HEIGHT = 32

def get_root_dir():
	return path.join(get_src_dir(), '..')

def get_src_dir():
	return path.dirname(__file__)
	
def get_art_dir():
	return path.join(get_root_dir(), 'assets', 'art')
	
def get_levels_dir():
	return path.join(get_src_dir(), 'levels')