import pygame
import settings
from players.player import Player


class Test_player(Player):
	def __init__(self, pos: tuple[int, int]):
		super().__init__(pos)

		# stats de base
		self.speed *= 1.1   # overrite plarent class sefault speed 
		self.image = pygame.image.load("../assets/character.png")
