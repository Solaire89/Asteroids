# this allows us to use code from
# the open-source pygame library
# throughout this file

import sys
import pygame # type: ignore
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_variable = pygame.time.Clock()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for sprite in updatable:
            sprite.update(dt)
        for shot in shots:
            if (shot.position.x > SCREEN_WIDTH or shot.position.x < 0 or
                shot.position.y > SCREEN_HEIGHT or shot.position.y < 0):
                shots.remove(shot)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.split()
                    shot.kill()
        for sprite in asteroids:
            if player.collisions(sprite):
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        time_passed = clock_variable.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__":
    main()