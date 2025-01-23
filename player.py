import pygame # type: ignore
from Solaire89.Asteroids.circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y, radius, PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.PLAYER_RADIUS = PLAYER_RADIUS
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]