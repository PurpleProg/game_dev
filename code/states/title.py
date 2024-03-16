import pygame
import settings
from states.state import State
from states.gameworld import GameWorld


class Title(State):
	def __init__(self, game) -> None:
		super().__init__(game)
		self.game = game

	def update(self, delta_time: float, pressed_keys: dict[str, bool]) -> None:

		# to remove, this is call every frame ( = not good)
		pygame.display.set_caption("Game - Title screen")

		if pressed_keys['RETURN']:
			new_state = GameWorld(self.game)
			new_state.enter_state()

	def render(self, canvas: pygame.Surface) -> None:
		canvas.fill(color=(0, 0, 255))
