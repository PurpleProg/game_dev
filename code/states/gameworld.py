import pygame
import settings
from states.state import State


class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)
        self.game = game

    def update(self, delta_time: float, pressed_keys: dict[str: bool]):

        # to remove, this is call every frame ( = not good)
        pygame.display.set_caption("Game - Main Game world screen")

        if pressed_keys['ESCAPE']:
            self.game.reset_pressed_keys()
            self.exit_state()

    def render(self, surface: pygame.Surface):
        temp_maingame_surface = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        temp_maingame_surface.fill(color=(0, 255, 0))
        surface.blit(temp_maingame_surface, dest=(0, 0))
