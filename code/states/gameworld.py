import pygame
import settings
from states.state import State
from states.pause import Pause
from players.test_player import Test_player


class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.player = Test_player(tuple((100, 100)))

    def update(self, delta_time: float, pressed_keys: dict[str: bool]):

        # this is done every frame (=not good for perf), pls fix it
        pygame.display.set_caption("Game - Main Game world screen")

        self.player.update(pressed_keys)

        if pressed_keys['ESCAPE']:
            self.game.reset_pressed_keys()
            new_state = Pause(self.game)
            new_state.enter_state()
        
        if pressed_keys['UP'] or pressed_keys['DOWN']:
            self.player.move_y(delta_time)
        if pressed_keys['RIGHT'] or pressed_keys['LEFT']:
            self.player.move_x(delta_time)

        # normalize diagonal movement
        if self.player.movement.length() > 1:
            self.player.movement.normalize()

    def render(self, surface: pygame.Surface):

        surface.fill(color=(0, 255, 0))

        # render the player
        self.player.render(surface)        
