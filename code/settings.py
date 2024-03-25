WIDTH, HEIGHT = 1024, 512

# cam rectangle
MIN_X, MAX_X = WIDTH*.1, WIDTH*.9
MIN_Y, MAX_Y = HEIGHT*.1, HEIGHT*.9

FPS = 120
FIXED_FPS = 60  # NEVER change that value otherwise the framerate independence breaks
TILE_SIZE = 16

# players
SPEED = 10
MAX_VELOCITY = 30*SPEED
