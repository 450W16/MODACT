import pygame
from utils import *
import level
from player import Player

def main():
	# initialize pygame
	pygame.init()

	# initialize screen
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("This is a game... or is it")

	player = Player()
	player.rect.x = 300
	player.rect.y = SCREEN_HEIGHT - player.rect.height
	# create sprite grouping for active sprites
	active_sprites = pygame.sprite.Group()
	active_sprites.add(player)

	done = False
	clock = pygame.time.Clock()
	screen.fill((0,0,0))

	while not done:
		for event in pygame.event.get()	:
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.move_left()
				if event.key == pygame.K_RIGHT:
					player.move_right()
				if event.key == pygame.K_SPACE:
					player.jump()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.delta_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.delta_x > 0:
					player.stop()
		
		# fill screen
		screen.fill((0,0,0))

		#update player
		active_sprites.update()

		# draw
		active_sprites.draw(screen)
	
		#FPS		
		clock.tick(60)
		
		#refresh screen
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
