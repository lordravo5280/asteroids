from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)

        self.position = pygame.math.Vector2(x, y)
        self.velocity = velocity or pygame.math.Vector2(random.uniform(-10, 10), random.uniform(-10, 10))

        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroid_list):
       self.kill()
       if self.radius <= ASTEROID_MIN_RADIUS:
           return
           
       random_angle = random.uniform(20, 50)
       left_vector = self.velocity.rotate(random_angle)
       right_vector = self.velocity.rotate(- random_angle)
       new_radius = self.radius - ASTEROID_MIN_RADIUS
       asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, left_vector * 1.2)
       asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, right_vector * 1.2)
       asteroid_list.add(asteroid1)
       asteroid_list.add(asteroid2)
