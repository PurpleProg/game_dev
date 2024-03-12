import pygame
import settings


class Player:
    def __init__(self, pos: tuple[int, int]):
        self.image = pygame.image.load("../assets/character.png")
        self.pos = pygame.math.Vector2(pos)
        self.speed = settings.SPEED
        self.direction = pygame.math.Vector2(0, 0)
        
    def render(self, surface: pygame.Surface):
        surface.blit(self.image, self.pos)

    def move_x(self, dt: float, ):
        self.pos.x += self.direction.x * self.speed * dt

    def move_y(self, dt: float):
        self.pos.y += self.direction.y * self.speed * dt
