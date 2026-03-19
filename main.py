import pygame
from constants import *
from logger import log_state
from player import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player_one = Player(x, y)




    game_state = 1

    while game_state == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()
        log_state()
        
        dt = fps_clock.tick(60)/1000

        
        #print(dt)


if __name__ == "__main__":
    main()
