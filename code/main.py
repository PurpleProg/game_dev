from game import Game

if __name__ == "__main__":
	game = Game()

	while game.running:
		game.main_loop()
		# self.offset_float.x += (player.rect.x - self.offset_float.x - settings.WIDTH/2) / 20
