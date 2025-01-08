# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # init a time object to set fps
    clock = pygame.time.Clock()
    dt = 0

    # init groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # init a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
        
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        
        pygame.display.flip()  # display update

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
    
    pygame.quit()




if __name__ == "__main__":
    main()