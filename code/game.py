import pygame, sys, time, os
from pygame.locals import *
import settings


class Game:
	def __init__(self):
		pygame.init()
		self.running = True
		self.playing = False

		# delta time related stuff
		self.clock = pygame.time.Clock()
		self.last_time: float = 0
		self.delta_time: float = 0

		# setting up the windows
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		pygame.display.set_caption("Game")
		pygame.display.set_icon(pygame.surface.Surface((10, 10)))

	def main_loop(self):
		# this is the main part of the code
		self.get_delta_time()
		self.get_events()
		self.update()
		self.render(self.screen)

	def get_delta_time(self):
		now = time.time()
		self.delta_time = now - self.last_time
		self.last_time = now

	def get_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.playing = False
				self.running = False
				pygame.quit()
				sys.exit()

	def update(self):
		pygame.display.flip()
		self.clock.tick(settings.FPS)

	def render(self, surface: pygame.Surface):
		test_surface = pygame.Surface((settings.WIDTH, settings.HEIGHT))
		test_surface.fill(color=(255, 255, 255))
		surface.blit(test_surface, dest=(0, 0))
