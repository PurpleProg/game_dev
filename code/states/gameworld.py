import pygame
import settings
from states.state import State
from states.pause import Pause
from players.test_player import Test_player
from levels.level_1 import Level_1
from camera import Camera


class GameWorld(State):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.game = game
        self.camera = Camera()
        self.player = Test_player(self.game, self.camera, pos=(settings.WIDTH/2, settings.HEIGHT/2))
        self.level = Level_1(self, self.camera)

    def update(self, delta_time: float, pressed_keys: dict[str,  bool]) -> None:

        # this is done every frame (=not good for perf), pls fix it
        pygame.display.set_caption("Game - Main Game world screen")

        # update player direction and movements
        self.player.update(pressed_keys, delta_time)

        # update the scroll variables
        self.camera.scroll(self.player)

        # update tiles position
        self.level.update()

        # quit state
        if pressed_keys['ESCAPE']:
            self.game.reset_pressed_keys()
            new_state = Pause(self.game)
            new_state.enter_state()

    def render(self, canvas: pygame.Surface) -> None:
        canvas.fill(color=(0, 255, 0))

        self.game.debug(self.player.rect.topleft, canvas, pos=(10, 50))

        # render the map
        self.level.render(canvas)

        # render the player
        self.player.render(canvas)        
