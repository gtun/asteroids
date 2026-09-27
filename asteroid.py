import circleshape
import pygame
import constants
import logger
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        #unit_vector = pygame.Vector2(0, 1)
        #rotated_vector = unit_vector.rotate(self.rotation)
        #rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        logger.log_event("asteroid_split")
        split_angle = random.uniform(20,50)
        new_asteroid_a = self.velocity.rotate(split_angle)
        new_asteroid_b = self.velocity.rotate(-split_angle)
        new_asteroid_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_a.velocity = new_asteroid_a * 1.2
        asteroid_b.velocity = new_asteroid_b * 1.2