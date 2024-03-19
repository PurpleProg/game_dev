import pygame
import settings


class Player(pygame.sprite.Sprite):
    """ parent class of all main characters """
    def __init__(self, game, camera,  pos: tuple[int, int]) -> None:
        super().__init__()
        self.game = game
        self.camera = camera

        # movement vars
        self.position = pygame.math.Vector2(pos)
        self.speed = pygame.Vector2(settings.SPEED, settings.SPEED)
        self.acceleration = pygame.math.Vector2(1.05, .4)
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.momentum = pygame.math.Vector2(0, 0)
        self.friction = .9

        # default values are overwrite by each character
        self.image = pygame.Surface(size=(settings.TILE_SIZE, settings.TILE_SIZE    ))
        self.image.fill(color=(255, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.prev_rect = self.rect.copy()

    def update(self, pressed_keys: dict[str, bool], dt: float) -> None:
        self.prev_rect = self.rect.copy()

        self.get_direction(pressed_keys)

        # for scrolling
        self.position += self.camera.offset_float

        self.move_x(dt)
        self.collide_x()
        self.camera.scroll_x(self)

        self.move_y(dt)
        self.collide_y()
        self.camera.scroll_y(self)

    def get_direction(self, pressed_keys: dict[str, bool]) -> None:
        if pressed_keys['UP']:
            self.direction.y = -1
            self.momentum.y = -self.acceleration.y
        elif pressed_keys['DOWN']:
            self.direction.y = 1
            self.momentum.y = self.acceleration.y
        else:
            self.direction.y = 0
            self.momentum.y = 0

        if pressed_keys['RIGHT']:
            self.direction.x = 1
            self.momentum.x = self.acceleration.x
        elif pressed_keys['LEFT']:
            self.direction.x = -1
            self.momentum.x = -self.acceleration.x
        else:
            self.direction.x = 0
            self.momentum.x = 0

        # fix diagonal movement
        if self.direction.length() > 1:
            self.direction = self.direction.normalize()

    def move_x(self, dt: float) -> None:
        self.velocity.x += self.speed.x * self.direction.x + self.momentum.x
        self.velocity.x *= self.friction
        self.limit_x_vel()
        self.position.x += self.velocity.x * dt
        self.rect.x = self.position.x

    def move_y(self, dt: float) -> None:
        self.velocity.y += self.speed.y * self.direction.y + self.momentum.y
        self.velocity.y *= self.friction
        self.limit_y_vel()
        self.position.y += self.velocity.y * dt
        self.rect.y = self.position.y

    def limit_x_vel(self) -> None:
        if abs(self.velocity.x) < 1 :
            self.velocity.x = 0
        if abs(self.velocity.x) > settings.MAX_VELOCITY:
            self.velocity.x = settings.MAX_VELOCITY if self.velocity.x > 0 else -settings.MAX_VELOCITY

    def limit_y_vel(self) -> None:
        if abs(self.velocity.y) < 1:
            self.velocity.y = 0
        if abs(self.velocity.y) > settings.MAX_VELOCITY:
            self.velocity.y = settings.MAX_VELOCITY if self.velocity.y > 0 else -settings.MAX_VELOCITY

    def collide_x(self):
        # player is from gameworld state, so here the stack is always gameworld.
        collided = pygame.sprite.spritecollide(self, self.game.stack[-1].level.tiles, dokill=False)

        if collided:
            for tile in collided:
                # from the left                
                if self.rect.right >= tile.rect.left and self.prev_rect.right <= tile.prev_rect.left:
                    print(tile.prev_rect.x, self.rect.x)
                    self.rect.right = tile.rect.left
                    self.position.x = self.rect.x
                # comming from the right
                elif self.rect.left <= tile.rect.right and self.prev_rect.left >= tile.prev_rect.right:
                    self.rect.left = tile.rect.right
                    self.position.x = self.rect.x

            self.velocity.x = 0

    def collide_y(self):
        # player is from gameworld state, so here the stack is always gameworld.
        collided = pygame.sprite.spritecollide(self, self.game.stack[-1].level.tiles, False)

        if collided:
            for tile in collided:
                # comming from the top
                if self.rect.bottom >= tile.rect.top and self.prev_rect.bottom <= tile.prev_rect.top:
                    self.rect.bottom = tile.rect.top
                    self.position.y = self.rect.y
                # from the bottom
                elif self.rect.top <= tile.rect.bottom and self.prev_rect.top >= tile.prev_rect.bottom:
                    self.rect.top = tile.rect.bottom
                    self.position.y = self.rect.y

            self.velocity.xy = (0, 0)

    def render(self, canvas: pygame.Surface) -> None:
        canvas.blit(source=self.image, dest=self.rect.topleft)
