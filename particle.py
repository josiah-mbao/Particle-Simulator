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

    def update(self, particles):
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x < self.radius or self.x > SCREEN_WIDTH - self.radius:
            self.vx *= -1
        if self.y < self.radius or self.y > SCREEN_HEIGHT - self.radius:
            self.vy *= -1

         # Collision detection with other particles
        for particle in particles:
            if particle != self:
                dx = particle.x - self.x
                dy = particle.y - self.y
                distance = (dx ** 2 + dy ** 2) ** 0.5
                if distance <= 2 * self.radius:
                    # Handle collision
                    self.handle_collision(particle)


    def handle_collision(self, other):
        # Simple elastic collision - swap velocities
        self.vx, other.vx = other.vx, self.vx
        self.vy, other.vy = other.vy, self.vy   


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
