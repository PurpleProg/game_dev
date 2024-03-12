from game import Game

# ok, player is working
from player import Player
player = Player()

if __name__ == "__main__":
	game = Game()
	while game.running:
		game.main_loop()