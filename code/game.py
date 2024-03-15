import pygame, sys, time, os
import settings
from states.title import Title


class Game:
	def __init__(self) -> None:
		pygame.init()
		self.running = True
		self.playing = False

		# states manager stack
		self.stack = []
		self.title_screen = Title(self)
		self.title_screen.enter_state()

		# delta time related stuff
		self.clock = pygame.time.Clock()
		self.last_time: float = 0
		self.delta_time: float = 0

		# setting up the windows
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		pygame.display.set_caption("Game")
		pygame.display.set_icon(pygame.surface.Surface((10, 10)))

		# and the canvas
		self.canvas = pygame.Surface(size=(settings.WIDTH, settings.HEIGHT))

		# setting up pressed_keys
		self.pressed_keys = {
			'RETURN': False,
			'ESCAPE': False,
			'UP': False,
			'DOWN': False,
			'RIGHT': False,
			'LEFT': False,
			'f': False,
		}

		self.count_temp = 0


	def main_loop(self) -> None:
		# this is the main part of the code
		self.get_delta_time()
		self.get_events()
		self.update()
		
		self.count_temp += 1
		if self.count_temp > settings.FPS:
			print(round(1/self.delta_time))
			self.count_temp = 0

		self.render()

	def get_delta_time(self) -> None:
		now = time.time()
		self.delta_time = now - self.last_time
		self.last_time = now

	def get_events(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				match event.key:
				# ENTER = RETURN, it's the "entrer" key
					case pygame.K_RETURN:
						self.pressed_keys['RETURN'] = True
					case pygame.K_ESCAPE:
						self.pressed_keys['ESCAPE'] = True
					case pygame.K_UP:
						self.pressed_keys['UP'] = True
					case pygame.K_DOWN:
						self.pressed_keys['DOWN'] = True
					case pygame.K_RIGHT:
						self.pressed_keys['RIGHT'] = True
					case pygame.K_LEFT:
						self.pressed_keys['LEFT'] = True
					case pygame.K_f:
						self.pressed_keys['f'] = True

			if event.type == pygame.KEYUP:
				match event.key:
					case pygame.K_RETURN:
						self.pressed_keys['RETURN'] = False
					case pygame.K_ESCAPE:
						self.pressed_keys['ESCAPE'] = False
					case pygame.K_UP:
						self.pressed_keys['UP'] = False
					case pygame.K_DOWN:
						self.pressed_keys['DOWN'] = False
					case pygame.K_RIGHT:
						self.pressed_keys['RIGHT'] = False
					case pygame.K_LEFT:
						self.pressed_keys['LEFT'] = False
					case pygame.K_f:
						self.pressed_keys['f'] = False

	def update(self) -> None:
		# run the update fonction of the last state of the stack

		if self.pressed_keys['f']:
			settings.FPS = 10 if settings.FPS == 60 else 60

		self.stack[-1].update(self.delta_time, self.pressed_keys)

	def render(self) -> None:
		# render the current state
		self.stack[-1].render(self.canvas)
		self.screen.blit(self.canvas, dest=(0, 0))

		# update the screen
		pygame.display.flip()

		# run at fixed FPS (well not exactly but there is delta_time for the lags)
		self.clock.tick(settings.FPS)

	# util methods
	def reset_pressed_keys(self) -> None:
		for key in self.pressed_keys.keys():
			self.pressed_keys[key] = False
