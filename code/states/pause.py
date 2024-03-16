import pygame
from settings import *
from states.state import State


class Pause(State):
	def __init__(self, game) -> None:
		super().__init__(game)
		self.game = game
		pygame.display.set_caption('pause')

	def update(self, delta_time: float, pressed_keys: dict[str, bool]) -> None:
		if pressed_keys['ESCAPE']:
			# we could only reset the escape key so we can pause buffer inputs
			self.game.reset_pressed_keys()
			self.exit_state()

	def render(self, canvas: pygame.Surface) -> None:
		canvas.fill(color=(255, 255, 0)) # yellow

