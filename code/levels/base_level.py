import pygame


class Base_level:
	def __init__(self, game):
		self.game = game

	def render(self, canvas: pygame.Surface) -> None:
		raise NotImplementedError
