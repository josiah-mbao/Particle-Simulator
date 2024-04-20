# particle.py
import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Particle:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.vx = 2
        self.vy = 1
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = 6

    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x < self.radius or self.x > SCREEN_WIDTH - self.radius:
            self.vx *= -1
        if self.y < self.radius or self.y > SCREEN_HEIGHT - self.radius:
            self.vy *= -1

        

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
