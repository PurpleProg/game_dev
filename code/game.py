import pygame
from pygame.locals import *
import sys
import settings


class Game:
	def __init__(self):
		self.playing = True
		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

	def run(self):
		# this is the main part of the code

		# from there, we need to use a game state manager (or gsm) but idk how to do this properly
		# for switching from Pause to playing or cinematiques

		# pygame mainloop
		while self.playing:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
