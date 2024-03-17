import pygame, settings


class Tile(pygame.sprite.Sprite):
	def __init__(self, pos: tuple[int, int]) -> None:
		super().__init__()
		self.pos = pos
		self.image = pygame.Surface(size=(settings.TILE_SIZE, settings.TILE_SIZE))
		self.image.fill(color=(255, 0, 0))
		self.rect = self.image.get_rect(topleft=self.pos)
		self.prev_rect = self.rect.copy()