import pygame
import settings
from states.state import State
from player import Player


class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.player = Player(pos=(100, 100))

    def update(self, delta_time: float, pressed_keys: dict[str: bool]):

        # to remove, this is call every frame ( = not good)
        pygame.display.set_caption("Game - Main Game world screen")

        self.player.update(pressed_keys)

        if pressed_keys['ESCAPE']:
            self.game.reset_pressed_keys()
            self.exit_state()
        
        if pressed_keys['UP'] or pressed_keys['DOWN']:
            self.player.move_y(delta_time)
        if pressed_keys['RIGHT'] or pressed_keys['LEFT']:
            self.player.move_x(delta_time)

    def render(self, surface: pygame.Surface):

        surface.fill(color=(0, 255, 0))

        # render the player
        self.player.render(surface)        
