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
        self.ACCELERATION = pygame.math.Vector2(.4, .4)  # stat
        self.friction = -.08

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

    def move_x(self, dt: float, ) -> None:
        dt = (dt * settings.FIXED_FPS)
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_x_vel(self.speed.x)
        self.position.x += self.velocity.x * dt + self.acceleration.x * dt 
        self.rect.x = self.position.x


    def move_y(self, dt: float) -> None:
        dt = (dt * settings.FIXED_FPS)
        self.acceleration.y += self.velocity.y * self.friction
        self.velocity.y += self.acceleration.y * dt
        self.limit_y_vel(self.speed.y)
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        self.rect.y = self.position.y

    def limit_x_vel(self, max_vel: int) -> None:
        # min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .1 : self.velocity.x = 0

    def limit_y_vel(self, max_vel: int) -> None:
        min(-max_vel, max(self.velocity.y, max_vel))  # idk wtf is this line doing
        if abs(self.velocity.y) < .1:
            self.velocity.y = 0

    def render(self, canvas: pygame.Surface) -> None:
        self.game.debug(self.velocity, canvas, pos=(10, 50))
        canvas.blit(source=self.image, dest=self.rect.center)
