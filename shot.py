import circleshape
import constants
import pygame

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        
    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
        
    def update(self, dt):
        #unit_vector = pygame.Vector2(0, 1)
        #rotated_vector = unit_vector.rotate(self.rotation)
        #rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += self.velocity * dt