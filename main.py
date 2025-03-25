import pygame, constants, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0,0,0))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
        for asteroid in asteroids:
            for bullet in shots:
                distance = ((asteroid.position[0] - bullet.position[0]) ** 2 + 
                    (asteroid.position[1] - bullet.position[1]) ** 2) ** 0.5
                if distance < (asteroid.radius + bullet.radius):
                    asteroid.split(asteroids)
                    bullet.kill()
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()