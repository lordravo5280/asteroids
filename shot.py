from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        self.velocity = pygame.Vector2(0, 1)
          
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 0)
    
    def update(self, dt):
        self.position += (self.velocity * dt)