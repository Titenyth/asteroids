from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_vel1 = self.velocity.rotate(angle)
            new_vel2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_aster1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_aster2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_aster1.velocity = new_vel1 * 1.2
            new_aster2.velocity = new_vel2 * 1.2
            for group in self.groups():
                group.add(new_aster1, new_aster2)
        