import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)

        dt = clock.tick(60) / 1000
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()