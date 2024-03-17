import pygame, settings, random
from levels.base_level import Base_level
from tiles.tile import Tile


class Level_1(Base_level):
	def __init__(self, game):
		super().__init__(game)
		self.game = game
		self.tiles = pygame.sprite.Group()

		test_gen_map = self.generate_map()

		self.read_2d_map(test_gen_map)

	def generate_map(self) -> list[list[int]]:
		map: list[list[int]] = []

		for row in range(int(settings.HEIGHT/settings.TILE_SIZE)):
			map.append([])
			for col in range(int(settings.WIDTH/settings.TILE_SIZE)):
				map[row].append([])
				if random.randint(1, 10) == 1:
					map[row][col] = 1
				else:
					map[row][col] = 0

		return map


	def render(self, canvas: pygame.Surface) -> None:
		# canvas.blit(self.test_surface, dest=(0, 0))
		self.tiles.draw(canvas)
