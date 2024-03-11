import pygame, sys, time, os
from pygame.locals import *
import settings
from states.title import Title


class Game:
	def __init__(self):
		pygame.init()
		self.running = True
		self.playing = False

		# states manager stack
		self.stack = []
		self.title_screen = Title(self)
		self.stack.append(self.title_screen)

		# delta time related stuff
		self.clock = pygame.time.Clock()
		self.last_time: float = 0
		self.delta_time: float = 0

		# setting up the windows
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		pygame.display.set_caption("Game")
		pygame.display.set_icon(pygame.surface.Surface((10, 10)))

		# setting up keys
		self.keys = {
			'ENTER': False,
			'ESCAPE': False
		}

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
			if event.type == KEYDOWN:
				if envent.key == K_ENTER:
					self.keys['ENTER'] = True
				if envent.key == K_ESC:
					self.keys['ESCAPE'] = True


	def update(self):

		self.stack[-1].update(self.delta_time, self.keys)

		pygame.display.flip()
		self.clock.tick(settings.FPS)

	def render(self, surface: pygame.Surface):
		# test_surface = pygame.Surface((settings.WIDTH, settings.HEIGHT))
		# test_surface.fill(color=(255, 255, 255))
		# surface.blit(test_surface, dest=(0, 0))
		self.stack[-1].render(self.screen)
