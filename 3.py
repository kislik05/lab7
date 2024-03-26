import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Перемещение шарика")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2
radius = 40

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 20 if y - radius >= 0 else 0
            elif event.key == pygame.K_DOWN:
                y += 20 if y + radius <= SCREEN_HEIGHT else 0
            elif event.key == pygame.K_LEFT:
                x -= 20 if x - radius >= 0 else 0
            elif event.key == pygame.K_RIGHT:
                x += 20 if x + radius <= SCREEN_WIDTH else 0

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (x, y), 25)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
