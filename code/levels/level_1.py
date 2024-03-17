import pygame, settings, random
from levels.base_level import Base_level
from tiles.tile import Tile


class Level_1(Base_level):
	def __init__(self, game):
		super().__init__(game)
		self.game = game


		temp_map = [
			[1, 1, 1],
			[1, 1, 1, 1],
			[1, 2, 2],
		]

		test_gen_map = self.generate_map()

		self.tiles = self.read_2d_map(test_gen_map)

	def read_2d_map(self, map: list[list[int, ...]]) -> pygame.sprite.Group:

		# test_surface = pygame.Surface(size=(settings.WIDTH, settings.HEIGHT))
		# test_surface.fill(color=(255, 0, 255))

		tiles = pygame.sprite.Group()

		# read the map
		for row_index, row_data in enumerate(map):
			for col_index, id in enumerate(row_data):
				pos = col_index*settings.TILE_SIZE, row_index*settings.TILE_SIZE
				match id:
					case 0:
						pass
					case 1:
						tile = Tile(pos)
						tiles.add(tile)
						# test_surface.blit(tile.image, dest=(col_index*settings.TILE_SIZE, row_index*settings.TILE_SIZE))
					case 2:
						pass
		return tiles

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
