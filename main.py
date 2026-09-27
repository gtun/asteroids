import pygame
import player
import asteroidfield
import asteroid
import shot
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    player.Player.containers = (updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    shot.Shot.containers = (drawable, updatable, shots)
    
    ship = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = asteroidfield.AsteroidField()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for oh_no_an_asteroid in asteroids:
            if oh_no_an_asteroid.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                svs.exit()
            for ah_yes_a_shot in shots:
                if oh_no_an_asteroid.collides_with(ah_yes_a_shot):
                    oh_no_an_asteroid.split()
                    ah_yes_a_shot.kill()
                    log_event("asteroid_shot")
        
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()