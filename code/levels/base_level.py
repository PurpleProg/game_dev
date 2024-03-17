import pygame, settings
from tiles.tile import Tile


class Base_level:
	def __init__(self, game):
		self.game = game

	def read_2d_map(self, map: list[list[int, ...]]) -> pygame.sprite.Group:
		# read the map
		for row_index, row_data in enumerate(map):
			for col_index, id in enumerate(row_data):
				pos = col_index*settings.TILE_SIZE, row_index*settings.TILE_SIZE
				match id:
					case 0:
						pass
					case 1:
						tile = Tile(pos)
						self.tiles.add(tile)
					case 2:
						pass

	def render(self, canvas: pygame.Surface) -> None:
		raise NotImplementedError