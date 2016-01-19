import pygame
import utils

def main():
	pygame.init()

	size = [utils.SCREEN_WIDTH, utils.SCREEN.HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("This is a game... or is it")
	

if __name__ == "__main__":
	main()
