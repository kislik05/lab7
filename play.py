import pygame
import random
import time
"""
import time
s = 100
for i in range(len(s)):
    level += 1
    time.sleep(5)
    print(s)
"""
pygame.init()

screen = pygame.display.set_mode((600, 600))

done = False
a = -60
b = 0
x = 0
y = 0 
speed = 10  # Set the speed for movement
move = 10
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
            if y != 540:
                y += speed
            else:
                y += 0
    if keys[pygame.K_UP]:
            if y != 0:
                y -= speed
            else:
                y -= 0
    if keys[pygame.K_RIGHT]:
            if x != 540:
                x += speed
            else:
                x += 0
    if keys[pygame.K_LEFT]:
            if x != 0:
                x -= speed
            else:
                x -= 0
    if b != 540: 
        b += move 
    else:
        b = -40
        a = random.randint(0, 540) 
    if x < a + 60 and x + 40 > a and y < b + 60 and y + 40 > b:
        done = True
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 40, 40))
    
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(a, b, 60, 60))

    pygame.display.flip()
    clock.tick(70)  
pygame.quit()

