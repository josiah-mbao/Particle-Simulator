import pygame
from particle import Particle, Obstacle
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, NUM_PARTICLES

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update_particles():
    for particle in particles:
        particle.update(particles, obstacles)

def draw_objects(screen):
    screen.fill((0, 0, 0))
    for particle in particles:
        particle.draw(screen)
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle.color, (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
    pygame.display.flip()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Particle Simulation")
clock = pygame.time.Clock()

# Create particles
particles = [Particle() for _ in range(NUM_PARTICLES)]

# Create obstacles
obstacles = [
    Obstacle(x=100, y=200, width=50, height=100, color=(255, 255, 255)),
    Obstacle(x=300, y=100, width=80, height=80, color=(255, 255, 255)),
    # Add more obstacles as needed
]

# Main loop
running = True
while running:
    running = handle_events()
    update_particles()
    draw_objects(screen)
    clock.tick(60)

# Quit Pygame
pygame.quit()
