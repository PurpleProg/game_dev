import pygame, settings


class Camera:
	def __init__(self) -> None:
		self.offset_float = pygame.math.Vector2(0, 1)
		self.offset_int = pygame.math.Vector2()
		# self.offset_int = self.offset_float.copy()  # here it's okay cause the settings are integers
		self.offset_int.x = int(self.offset_float.x)
		self.offset_int.y = int(self.offset_float.y)

	def scroll(self, player) -> None:

		# y
		if player.rect.y > settings.MAX_Y:
			self.offset_float.y = settings.MAX_Y - player.rect.y
			print(self.offset_float.y)
		elif player.rect.y < settings.MIN_Y:
			self.offset_float.y = settings.MIN_Y - player.rect.y
		else:
			self.offset_float.y = .0

		# x
		if player.rect.x > settings.MAX_X:
			self.offset_float.x = settings.MAX_X - player.rect.x
		elif player.rect.x < settings.MIN_X:
			self.offset_float.x = settings.MIN_X - player.rect.x
		else:
			self.offset_float.x = .0

		# self.offset_float.x += (player.rect.x - self.offset_float.x - settings.WIDTH/2) / 20
		# self.offset_float.y += (player.rect.y - self.offset_float.y - settings.HEIGHT/2) / 20
		self.offset_int.x = int(self.offset_float.x)
		self.offset_int.y = int(self.offset_float.y)
