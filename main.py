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

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    
    
    


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
        
        for obj in updatable:
            obj.update(dt)

        screen.fill((0,0,0))

        for obj in asteroids:
            if obj.detect_collision(player):
               print("Game over!")
               pygame.quit()
               return
                
            for shot in shots:
                if obj.detect_collision(shot):
                    print(f"{shot} and {obj}")
                    obj.split()
                    shot.kill()
                    break

           
        

        for obj in drawable:
            obj.draw(screen)
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()