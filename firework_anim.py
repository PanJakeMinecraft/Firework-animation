# Import the necessary libraries
import pygame
import random
import math
import sys

# Starting the pygame
pygame.init()

# Screen size and framerate
LENGTH, HEIGHT = 800, 600
FPS = 60

# Sceen color
BLACK = (4, 18, 62)

screen = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Fireworks animation")
clock = pygame.time.Clock()

# The fireworks
class Firework:
    def __init__(self):
        self.x = random.randint(50, LENGTH - 50)
        self.y = HEIGHT
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.explosion_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(3)]  
        self.radius = random.randint(5, 7)  
        self.explosion_radius = random.randint(7, 10) 
        self.speed = random.randint(5, 10)

    def move(self):
        self.y -= self.speed
        if self.y <= HEIGHT // 2:
            self.explode()

    def explode(self):
        particles = []
        for _ in range(100):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(7, 2)
            color = random.choice(self.explosion_colors)
            particle = Particle(self.x, self.y, angle, speed, color, self.explosion_radius)
            particles.append(particle)
        fireworks.remove(self)
        particles_group.add(particles)

# Particle when explosion
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed, color, radius):
        super().__init__()
        self.image = pygame.Surface((radius, radius))
        self.image.set_colorkey(BLACK)  
        pygame.draw.circle(self.image, color, (radius // 2, radius // 2), radius // 2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = speed

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)
        self.speed -= 0.05
        if self.speed <= 0:
            self.kill()

# Looping the fireworks and the explosion of fireworks
fireworks = []
particles_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Create a new firework at the bottom
    if random.random() < 0.03:
        fireworks.append(Firework())

    # Update fireworks and particles
    for firework in fireworks:
        firework.move()

    particles_group.update()

    # Draw the fireworks and screen
    screen.fill(BLACK)  
    for firework in fireworks:
        pygame.draw.circle(screen, firework.color, (firework.x, int(firework.y)), firework.radius)
    particles_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)