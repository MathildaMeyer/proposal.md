import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxia 2.0 - Interactive Cosmic Generative Art")

# Colors
BLACK = (0, 0, 20)  # Space background
STAR_COLORS = [(255, 255, 255), (200, 200, 255), (255, 220, 180), (180, 255, 200)]

# Celestial Body Class
class CelestialBody:
    def __init__(self, x, y, size, speed, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.angle = random.uniform(0, 2 * math.pi)  # Random initial direction

    def move(self):
        """Moves the celestial body in a wave-like motion."""
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.angle += random.uniform(-0.05, 0.05)  # Slight variation in movement

        # Wrap around screen edges
        if self.x < 0: self.x = WIDTH
        if self.x > WIDTH: self.x = 0
        if self.y < 0: self.y = HEIGHT
        if self.y > HEIGHT: self.y = 0

    def draw(self):
        """Draws the celestial body on the screen."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Generate initial celestial bodies
bodies = [CelestialBody(random.randint(0, WIDTH), random.randint(0, HEIGHT), 
                         random.randint(2, 6), random.uniform(0.5, 2.0), 
                         random.choice(STAR_COLORS)) for _ in range(100)]

# Main loop
running = True
speed_factor = 1.0  # Default speed multiplier

while running:
    screen.fill(BLACK)  # Dark cosmic background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls for interactivity
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Increase celestial bodies
                bodies.append(CelestialBody(random.randint(0, WIDTH), random.randint(0, HEIGHT), 
                                           random.randint(2, 6), random.uniform(0.5, 2.0), 
                                           random.choice(STAR_COLORS)))
            if event.key == pygame.K_DOWN and len(bodies) > 0:  # Reduce celestial bodies
                bodies.pop()
            if event.key == pygame.K_LEFT:  # Slow down motion
                speed_factor *= 0.9
            if event.key == pygame.K_RIGHT:  # Speed up motion
                speed_factor *= 1.1
            if event.key == pygame.K_c:  # Change colors dynamically
                for body in bodies:
                    body.color = random.choice(STAR_COLORS)

    # Update and draw celestial bodies with adjusted speed
    for body in bodies:
        body.speed *= speed_factor
        body.move()
        body.draw()

    pygame.display.flip()  # Refresh screen

pygame.quit()


