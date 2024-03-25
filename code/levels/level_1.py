import pygame, settings, random
from levels.base_level import Base_level
from tiles.tile import Tile


class Level_1(Base_level):
	def __init__(self, gameworld, camera) -> None:
		super().__init__(gameworld)
		self.gameworld = gameworld
		self.camera = camera

		self.tiles = pygame.sprite.Group()
		test_gen_map = self.generate_map()

		self.read_2d_map(test_gen_map)

	def generate_map(self) -> list[list[int]]:
		map: list[list[int]] = []

		for row in range(int(settings.HEIGHT*3/settings.TILE_SIZE)):
			map.append([])
			for col in range(int(settings.WIDTH*3/settings.TILE_SIZE)):
				map[row].append([])
				if random.randint(1, 50) == 1:
					map[row][col] = 1
				else:
					map[row][col] = 0

		return map

	def update(self) -> None:
		for tile in self.tiles:
			tile.update(self.camera)

	def render(self, canvas: pygame.Surface) -> None:

		for tile in self.tiles:
			canvas.blit(tile.image, tile.rect.topleft)

