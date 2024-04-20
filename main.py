# main.py
import pygame
from particle import Particle
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, NUM_PARTICLES

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Particle Simulation")
clock = pygame.time.Clock()

# Create particles
particles = [Particle() for _ in range(NUM_PARTICLES)]

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    for particle in particles:
        particle.update()

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw particles
    for particle in particles:
        particle.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
