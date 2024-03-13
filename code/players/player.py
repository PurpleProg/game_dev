import pygame
import settings


class Player(pygame.sprite.Sprite):
    """ parent class of all main characters """
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        # self.pos = pygame.math.Vector2(pos)    # let's just use rect.center instead
        self.direction = pygame.math.Vector2(0, 0)
        self.movement = pygame.math.Vector2(0, 0)

        # default values are overwrite by each character
        self.image = pygame.Surface(size=(32, 32))
        self.image.fill(color=(255, 0, 0))
        self.rect = self.image.get_rect(center=pos)
        print(self.rect.centerx)

        self.speed = pygame.Vector2(settings.SPEED, settings.SPEED)

    def update(self, pressed_keys: dict[str: bool]):
        
        self.get_direction(pressed_keys)

        # fix diagonal movement
        if self.direction.length() > 1:
            self.direction.normalize()

    def get_direction(self, pressed_keys: dict[str: bool]):
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
        self.movement.x = self.direction.x * self.speed.x  # * dt

    def move_y(self, dt: float):
        self.movement.y = self.direction.y * self.speed.y  # * dt

    def render(self, surface: pygame.Surface):
        self.rect.center += self.movement
        self.movement.xy = (0, 0)
        surface.blit(source=self.image, dest=self.rect.center)
