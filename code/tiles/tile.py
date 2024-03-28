import pygame, settings


class Tile(pygame.sprite.Sprite):
	def __init__(self, pos: tuple[int, int]) -> None:
		super().__init__()
		# actual pos (float)
		self.pos = pygame.math.Vector2(pos[0], pos[1])

		# image
		self.image = pygame.Surface(size=(settings.TILE_SIZE, settings.TILE_SIZE))
		self.image.fill(color=(255, 0, 0))

		# less acurate but less buggy position (int)
		self.rect = self.image.get_rect(topleft=pos)
		self.prev_rect = self.rect.copy()

	def update(self, camera) -> None:

		self.prev_rect = self.rect.copy()

		self.pos += camera.offset_int
		self.rect.x, self.rect.y = self.pos.x, self.pos.y
