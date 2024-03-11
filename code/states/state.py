class State:
    def __init__(self, game):
        self.game = game

    def update(self, delta_time: float, pressed_keys: dict[str: bool]):
        raise NotImplementedError

    def render(self, surface):
        raise NotImplementedError

    def enter_state(self):
        if len(self.game.stack) > 1:
            self.game.previous_state = self.game.stack[-1]
        self.game.stack.append(self)

    def exit_state(self):
        self.game.stack.pop()
