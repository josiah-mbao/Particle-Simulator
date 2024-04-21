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
        self.mass = random.randint(1, 4)

    def update(self, particles):
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x < self.radius or self.x > SCREEN_WIDTH - self.radius:
            self.vx *= -1
        if self.y < self.radius or self.y > SCREEN_HEIGHT - self.radius:
            self.vy *= -1

        # List to store collision information
        collisions = []

         # Collision detection with other particles
        for particle in particles:
            if particle != self:
                dx = particle.x - self.x
                dy = particle.y - self.y
                distance = (dx ** 2 + dy ** 2) ** 0.5
                if distance <= 2 * self.radius:
                    # Handle collision
                    collisions.append((distance, particle))

         # Sort collisions based on impact (closest first)
        collisions.sort(key=lambda collision: collision[0])

        # Resolve collisions sequentially
        for collision in collisions:
            self.handle_collision(collision[1])


    def handle_collision(self, other):
        # Calculate contact information
        dx = other.x - self.x
        dy = other.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        nx = dx / distance  # Normal vector components
        ny = dy / distance

        # Calculate relative velocity along the contact normal
        relative_velocity = (self.vx - other.vx) * nx + (self.vy - other.vy) * ny

        # Calculate impulse (change in momentum)
        impulse = 2 * relative_velocity / (self.mass + other.mass)

        # Apply impulse to change velocities
        self.vx -= impulse * other.mass * nx
        self.vy -= impulse * other.mass * ny
        other.vx += impulse * self.mass * nx
        other.vy += impulse * self.mass * ny


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
