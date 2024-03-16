import pygame
import settings


class Player(pygame.sprite.Sprite):
    """ parent class of all main characters """
    def __init__(self, game,  pos: tuple[int, int]) -> None:
        super().__init__()
        self.game = game
        # self.pos = pygame.math.Vector2(pos)    # let's just use rect.center instead
        self.position = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)  # the value used in the calculs
        self.ACCELERATION = pygame.math.Vector2(1.05, .4)  # stat
        self.friction = .8

        # default values are overwrite by each character
        self.image = pygame.Surface(size=(32, 32))
        self.image.fill(color=(255, 0, 0))
        self.rect = self.image.get_rect()
        self.speed = pygame.Vector2(settings.SPEED, settings.SPEED)

    def update(self, pressed_keys: dict[str, bool], dt: float) -> None:
        self.get_direction(pressed_keys)
        self.move_x(dt)
        self.move_y(dt)

    def get_direction(self, pressed_keys: dict[str, bool]) -> None:
        self.acceleration.x = 0
        self.acceleration.y = 0

        if pressed_keys['UP']:
            self.direction.y = -1
            self.acceleration.y -= self.ACCELERATION.y
        elif pressed_keys['DOWN']:
            self.direction.y = 1
            self.acceleration.y += self.ACCELERATION.y
        else:
            self.direction.y = 0

        if pressed_keys['RIGHT']:
            self.direction.x = 1
            self.acceleration.x += self.ACCELERATION.x
        elif pressed_keys['LEFT']:
            self.direction.x = -1
            self.acceleration.x -= self.ACCELERATION.x
        else:
            self.direction.x = 0

        # fix diagonal movement
        if self.direction.length() > 1:
            self.direction = self.direction.normalize()

    def move_x(self, dt: float) -> None:
        self.velocity.x += self.speed.x * self.direction.x + self.acceleration.x
        self.velocity.x *= self.friction
        self.limit_x_vel()
        self.position.x += self.velocity.x * dt
        self.rect.x = self.position.x

    def move_y(self, dt: float) -> None:
        self.velocity.y += self.speed.y * self.direction.y + self.acceleration.y
        self.velocity.y *= self.friction
        self.limit_y_vel()
        self.position.y += self.velocity.y * dt
        self.rect.y = self.position.y

    def limit_x_vel(self) -> None:
        if abs(self.velocity.x) < .1 :
            self.velocity.x = 0
        if abs(self.velocity.x) > settings.MAX_VELOCITY:
            self.velocity.x = settings.MAX_VELOCITY if self.velocity.x > 0 else -settings.MAX_VELOCITY

    def limit_y_vel(self) -> None:
        if abs(self.velocity.y) < .1:
            self.velocity.y = 0
        if abs(self.velocity.y) > settings.MAX_VELOCITY:
            self.velocity.y = settings.MAX_VELOCITY if self.velocity.y > 0 else -settings.MAX_VELOCITY

    def render(self, canvas: pygame.Surface) -> None:
        canvas.blit(source=self.image, dest=self.rect.center)
