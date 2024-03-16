import pygame
import settings


class Player(pygame.sprite.Sprite):
    """ parent class of all main characters """
    def __init__(self, game,  pos: tuple[int, int]) -> None:
        super().__init__()
        self.game = game
        # self.pos = pygame.math.Vector2(pos)    # let's just use rect.center instead
        self.direction = pygame.math.Vector2(0, 0)
        self.movement = pygame.math.Vector2(0, 0)

        # default values are overwrite by each character
        self.image = pygame.Surface(size=(32, 32))
        self.image.fill(color=(255, 0, 0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = pygame.Vector2(settings.SPEED, settings.SPEED)

    def update(self, pressed_keys: dict[str, bool]) -> None:
        self.get_direction(pressed_keys)

    def get_direction(self, pressed_keys: dict[str, bool]) -> None:
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
            self.direction = self.direction.normalize()

    def move_x(self, dt: float, ) -> None:
        self.movement.x = self.direction.x * self.speed.x * (dt * 100)

    def move_y(self, dt: float) -> None:
        self.movement.y = self.direction.y * self.speed.y * (dt * 100)

    def render(self, canvas: pygame.Surface) -> None:
        self.rect.center += self.movement
        self.movement = pygame.math.Vector2(0, 0)
        canvas.blit(source=self.image, dest=self.rect.center)
