# mandatory pygame initialization
import pygame

pygame.init()



# other imports as needed
from constants import *

# the good stuff
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)  # black background
    while True:
        pygame.Surface.fill(screen, color)
        pygame.display.flip()

if __name__ == "__main__":
    main()
