import pygame
import settings
from players.player import Player


class Test_player(Player):
	def __init__(self, game, pos: tuple[int, int]) -> None:
		super().__init__(game, pos)
		self.game = game

		# stats de base
		self.speed *= 1.1   # overrite plarent class sefault speed 

		self.image = pygame.image.load("../assets/character.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (settings.TILE_SIZE, settings.TILE_SIZE))
		# self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect(topleft=pos)
		self.mask = pygame.mask.from_surface(self.image)
