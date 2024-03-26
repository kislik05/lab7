import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
def blitRotate(surf, image, pos, originPos, angle):
   
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)

image = pygame.image.load('leftarm.png')
image2 = pygame.image.load('rightarm.png')
image3 = pygame.image.load('mouse.png')
w, h = image.get_size()
d, e = image2.get_size()
angle = 0
angle2 = 0
done = False
sum = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width() / 2, screen.get_height() / 2)
    screen.fill(0)
    screen.blit(image3, (-250, -100))
    blitRotate(screen, image, pos, (w / 2, h / 2), angle)
    blitRotate(screen, image2, pos, (d / 2, e / 2), angle2)
    clock.tick(60)
    time.sleep(1)
    angle -= 6
    sum += 6
    if sum % 360 == 0:
        blitRotate(screen, image2, pos, (d / 2, e / 2), angle2)
        angle2 -= 6
    pygame.display.flip()

pygame.quit()
exit()
