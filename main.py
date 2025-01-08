# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # init a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # init a AsteroidField object
    asteroid_field = AsteroidField()

    loop = 1
    while loop:                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
        
        for obj in updatable:
            obj.update(dt)

        # collision check Player-Asteroids
        for obj in asteroids:
            if obj.collision_check(player):
                print("Game over!")
                loop = 0

        #collision check Shots-Asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        
        pygame.display.flip()  # display update

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
    
    pygame.quit()




if __name__ == "__main__":
    main()