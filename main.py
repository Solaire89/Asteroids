# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import *

def main():
    pygame.init()
    clock_variable = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        time_passed = clock_variable.tick(60)
        dt = time_passed / 1000
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

"""
This line ensures the main() function is only called when this file is run directly;
it won't run if it's imported as a module. 
It's considered the "pythonic" way to structure an executable program in Python. 
Technically, the program will work fine by just calling main(), 
but you might get an angry letter from Guido van Rossum if you don't.
"""