from states.state import State
import pygame
import settings

class Title(State):
	def __init__(self, game):
		super().__init__(game)
		self.game = game

	def update(self, delta_time: float, keys: dict[str: bool]):
		pass

	def render(self, surface):
		temp_title_surface = pygame.Surface((settings.WIDTH, settings.HEIGHT))
		temp_title_surface.fill(color=(0, 0, 255))
		surface.blit(temp_title_surface, dest=(0, 0))
