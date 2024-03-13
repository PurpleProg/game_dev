class State:
    def __init__(self, game) -> None:
        self.game = game

    def update(self, delta_time: float, pressed_keys: dict[str: bool]) -> None:
        raise NotImplementedError

    def render(self, surface) -> None:
        raise NotImplementedError

    def enter_state(self) -> None:
        if len(self.game.stack) > 1:
            self.game.previous_state = self.game.stack[-1]
        self.game.stack.append(self)

    def exit_state(self) -> None:
        self.game.stack.pop()
