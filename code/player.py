import pygame
import settings


class Player:
    def __init__(self, pos: tuple[int, int]):
        self.image = pygame.image.load("../assets/character.png")
        self.pos = pygame.math.Vector2(pos)
        self.speed = pygame.Vector2(settings.SPEED, settings.SPEED)
        self.direction = pygame.math.Vector2(0, 0)
        self.movement = pygame.math.Vector2(0, 0)

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

        # fix diagonal movement
        if self.direction.length() > 1:
            self.direction.normalize()

    def move_x(self, dt: float, ):
        self.movement.x = self.direction.x * self.speed.x # * dt

    def move_y(self, dt: float):
        self.movement.y = self.direction.y * self.speed.y # * dt

    def render(self, surface: pygame.Surface):
        self.pos += self.movement
        self.movement.xy = (0, 0)
        surface.blit(source=self.image, dest=self.pos)
