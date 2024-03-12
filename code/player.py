import pygame
import settings


class Player:
    def __init__(self, pos: tuple[int, int]):
        self.image = pygame.image.load("../assets/character.png")
        self.pos = pygame.math.Vector2(pos)
        self.speed = settings.SPEED
        self.direction = pygame.math.Vector2(0, 0)

    def update(self, pressed_keys: dict[str: bool]):
        if pressed_keys['UP']:
            self.direction.y = -1
        elif pressed_keys['DOWN']:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if pressed_keys['RIGHT']:
            self.direction.x = 1
        elif pressed_keys['LEFT']:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move_x(self, dt: float, ):
        self.pos.x += self.direction.x * self.speed # * dt

    def move_y(self, dt: float):
        self.pos.y += self.direction.y * self.speed # * dt

    def render(self, surface: pygame.Surface):
        surface.blit(source=self.image, dest=self.pos)
