import pygame
from settings import *

class Player():
    def __init__(self):
        self.image = pygame.image.load("character.png")
        self.x = 100
        self.y = 100
        self.speed = SPEED
        self.direction_x = 0
        self.direction_y = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_x(self, dt: float, ):
        if self.direction_x != 0:
            if self.direction_y !=0:
                self.x += self.direction_x * self.speed*0.75 * dt 
            else:
                self.x += self.direction_x * self.speed * dt 

    def move_y(self, dt: float):
        if self.direction_y != 0:
            if self.direction_x !=0:
                self.y += self.direction_y * self.speed*0.75 * dt 
            else:
                self.y += self.direction_y * self.speed * dt 
