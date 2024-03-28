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
        # kinematics vectors
        self.acceleration = pygame.math.Vector2(0, 0)
        self.ACCELERATION = pygame.math.Vector2(settings.FPS*1, settings.FPS*1)
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.friction = .20

        # default values are overwrite by each character
        self.image = pygame.Surface(size=(settings.TILE_SIZE, settings.TILE_SIZE))
        self.image.fill(color=(255, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.prev_rect = self.rect.copy()

    def update(self, pressed_keys: dict[str, bool], dt: float) -> None:
        self.prev_rect = self.rect.copy()

        self.get_direction(dt, pressed_keys)

        self.move_x(dt)
        self.camera.scroll_x(self)
        self.collide_x()

        self.move_y(dt)
        self.camera.scroll_y(self)
        self.collide_y()

        # scrolling
        self.position += self.camera.offset_float
        self.rect.x, self.rect.y = self.position.x, self.position.y

    def get_direction(self, dt: float, pressed_keys: dict[str, bool]) -> None:
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

        self.acceleration.x = self.direction.x * self.ACCELERATION.x * dt
        self.acceleration.y = self.direction.y * self.ACCELERATION.y * dt

    def move_x(self, dt: float) -> None:
        # update kinetics vectors
        self.acceleration.x -= self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x

        # avoid velocity get too close to 0
        self.velocity.x = 0 if self.velocity.x < 0.01 and self.velocity.x > -0.01 else self.velocity.x

        # change player position
        self.position.x += self.velocity.x + .5*self.acceleration.x #  * dt
        self.rect.x = self.position.x

    def move_y(self, dt: float) -> None:
        # update kinetics vectors
        self.acceleration.y -= self.velocity.y * self.friction
        self.velocity.y += self.acceleration.y

        # limit velocity becoming 1.98754e-70
        self.velocity.y = 0 if self.velocity.y < 0.01 and self.velocity.y > -0.01 else self.velocity.y

        # change player position
        self.position.y += self.velocity.y + .5*self.acceleration.y #  * dt
        self.rect.y = self.position.y

    def collide_x(self):
        # player is from gameworld state, so here the stack is always gameworld.
        collided = pygame.sprite.spritecollide(self, self.game.stack[-1].level.tiles, dokill=False)

        if collided:
            for tile in collided:
                # from the left                
                if self.rect.right >= tile.rect.left and self.prev_rect.right <= tile.prev_rect.left:
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

            self.velocity.y = 0

    def render(self, canvas: pygame.Surface) -> None:
        canvas.blit(source=self.image, dest=self.rect.topleft)
