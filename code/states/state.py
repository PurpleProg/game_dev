import pygame


class State:
    def __init__(self, game) -> None:
        self.game = game

    def update(self, delta_time: float, pressed_keys: dict[str: bool]) -> None:
        raise NotImplementedError

    def render(self, canvas: pygame.Surface) -> None:
        raise NotImplementedError

    def enter_state(self) -> None:
        """add itself to the top of the stack"""
        if len(self.game.stack) > 1:
            self.game.previous_state = self.game.stack[-1]
        self.game.stack.append(self)

    def exit_state(self) -> None:
        self.game.stack.pop()
