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

		# setting up pressed_pressed_keys
		self.pressed_keys = {
			'RETURN': False,
			'ESCAPE': False
		}

	def main_loop(self):
		# this is the main part of the code
		self.get_delta_time()
		self.get_events()

		# to remove, debug feature
		print(self.pressed_keys)

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
				# ENTER = RETURN, it's the "entrer" key
				if event.key == K_RETURN:
					self.pressed_keys['RETURN'] = True
				if event.key == K_ESCAPE:
					self.pressed_keys['ESCAPE'] = True
			if event.type == KEYUP:
				if event.key == K_RETURN:
					self.pressed_keys['RETURN'] = False
				if event.key == K_ESCAPE:
					self.pressed_keys['ESCAPE'] = False

	def update(self):
		self.stack[-1].update(self.delta_time, self.pressed_keys)

	def render(self, surface: pygame.Surface):
		# render the current state
		self.stack[-1].render(self.screen)

		# update the screen
		pygame.display.flip()

		# run at fixed FPS (well not exactly but there is delta_time for that)
		self.clock.tick(settings.FPS)

	def reset_pressed_pressed_keys(self):
		print("reseting pressed_pressed_keys")
		for key in self.pressed_keys.keys():
			self.pressed_keys[key] = False
