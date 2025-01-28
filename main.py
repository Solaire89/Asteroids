# this allows us to use code from
# the open-source pygame library
# throughout this file
from asteroid import Asteroid
import sys
import pygame # type: ignore
from constants import *
from player import Player
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
    Player.containers = (updatable, drawable)
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

"""
This line ensures the main() function is only called when this file is run directly;
it won't run if it's imported as a module. 
It's considered the "pythonic" way to structure an executable program in Python. 
Technically, the program will work fine by just calling main(), 
but you might get an angry letter from Guido van Rossum if you don't.
"""