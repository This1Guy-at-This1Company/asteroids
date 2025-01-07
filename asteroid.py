import pygame
from circleshape import *
from constants import *
import random



class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position ,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
    # Kill the current asteroid
        self.kill()

    # If the asteroid is too small, do nothing
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

    # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20.0, 50.0)

    # Rotate the current velocity to create two new vectors
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

    # Create two new asteroids at the current position with the new radius
        split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid1.velocity = new_velocity1

        split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid2.velocity = new_velocity2

